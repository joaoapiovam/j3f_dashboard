"""Generate the dashboard hero PNG following the Structural Resonance philosophy.

Output: assets/hero.png (1280 x 400, palette: J3F Brand 2026).

Philosophy reference:
docs/superpowers/specs/2026-05-07-hero-design-philosophy.md
(stored in the J3F_SPED_Analyzer repo, not in the dashboard repo).

Usage:
    python build_hero.py
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

WIDTH = 1280
HEIGHT = 400

VERDE_ESCURO = (0, 82, 99)
TEAL = (0, 172, 202)
VERDE_CLARO = (150, 201, 215)
COBRE = (158, 148, 126)


def _interp(c1: tuple[int, int, int], c2: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    """Linear interpolation between two RGB colors."""
    t = max(0.0, min(1.0, t))
    return tuple(int(round(c1[i] + (c2[i] - c1[i]) * t)) for i in range(3))


def _paint_field(img: Image.Image) -> None:
    """Two-stop horizontal field: deep verde escuro on the left, gently lifting toward
    a slightly warmer institutional teal on the right. No third stop — the brand
    forbids gradient theatrics. The lift is just enough to make the field feel awake."""
    pixels = img.load()
    end = (0, 90, 110)
    for x in range(WIDTH):
        t = x / (WIDTH - 1)
        smooth = 0.5 - 0.5 * math.cos(math.pi * t)
        col = _interp(VERDE_ESCURO, end, smooth * 0.55)
        for y in range(HEIGHT):
            pixels[x, y] = col


def _draw_line_field(img: Image.Image) -> None:
    """The line-field. Many vertical strokes anchored to the lower baseline,
    rising into a continuous sinusoidal envelope. Two full wavelengths so the
    pattern reads as rhythm, not as a single hill. The field fades at both ends
    via per-line opacity — the discipline of an instrument that knows where it
    starts and where it stops, never bleeding past its edges.

    Lines drawn on a 4x oversampled buffer then downsampled — the result is the
    crisp anti-aliased vertical edge that hand-drawn ink would give."""
    scale = 4
    over_w, over_h = WIDTH * scale, HEIGHT * scale
    over = Image.new("RGBA", (over_w, over_h), (0, 0, 0, 0))
    od = ImageDraw.Draw(over)

    spacing = 9
    line_w = 2
    n_lines = 110
    field_left = 80
    baseline_y = 286
    env_amp = 128
    cycles = 1.85
    env_phase = 0.32 * math.pi
    base_alpha = 220

    edge_fade = 0.18

    for i in range(n_lines):
        x_center = field_left + i * spacing
        env = math.sin((i / n_lines) * cycles * 2 * math.pi + env_phase)
        env_norm = (env + 1) * 0.5
        height = 18 + env_norm * env_amp

        edge_t = i / max(1, n_lines - 1)
        if edge_t < edge_fade:
            edge_alpha = (edge_t / edge_fade) ** 1.2
        elif edge_t > 1 - edge_fade:
            edge_alpha = ((1 - edge_t) / edge_fade) ** 1.2
        else:
            edge_alpha = 1.0

        alpha = int(base_alpha * edge_alpha)
        if alpha < 8:
            continue

        color = (*VERDE_CLARO, alpha)
        x_top = baseline_y - height
        x = x_center * scale
        y0 = x_top * scale
        y1 = baseline_y * scale
        od.rectangle(
            [x - (line_w * scale) // 2, y0, x + (line_w * scale) // 2, y1],
            fill=color,
        )

    over = over.resize((WIDTH, HEIGHT), Image.LANCZOS)
    img.paste(over, (0, 0), over)


def _draw_quiet_wave(img: Image.Image) -> None:
    """Two horizontal currents at slightly offset phases. Low amplitude.
    Lives in the lower register. This is the J3F signature wave, repurposed as
    a baseline rhythm — not a flourish. Two strokes are enough to register;
    three would announce themselves and break the discipline."""
    scale = 3
    over = Image.new("RGBA", (WIDTH * scale, HEIGHT * scale), (0, 0, 0, 0))
    od = ImageDraw.Draw(over)

    waves = [
        {"y": 322, "amp": 18, "period": 820, "phase": 0.0,        "alpha": 175, "thick": 1.6},
        {"y": 350, "amp": 12, "period": 980, "phase": 0.6 * math.pi, "alpha": 95, "thick": 1.2},
    ]

    for w in waves:
        color = (*TEAL, w["alpha"])
        samples = []
        for x in range(0, WIDTH + 1, 2):
            y = w["y"] + w["amp"] * math.sin((x / w["period"]) * 2 * math.pi + w["phase"])
            samples.append((x * scale, y * scale))
        for (x0, y0), (x1, y1) in zip(samples, samples[1:]):
            od.line([x0, y0, x1, y1], fill=color, width=int(w["thick"] * scale))

    over = over.filter(ImageFilter.GaussianBlur(radius=0.5))
    over = over.resize((WIDTH, HEIGHT), Image.LANCZOS)
    img.paste(over, (0, 0), over)


def _draw_dot_grid(img: Image.Image) -> None:
    """Calibration grid in the right third. Sparse. Cobre at low opacity.
    Suggests measurement without insisting on it. Falloff is radial from the
    densest corner (upper-right) and decays with a soft curve so the grid
    appears to have always been there, never planted in a moment."""
    scale = 2
    over = Image.new("RGBA", (WIDTH * scale, HEIGHT * scale), (0, 0, 0, 0))
    od = ImageDraw.Draw(over)

    grid_left = 720
    grid_right = WIDTH - 48
    grid_top = 56
    grid_bottom = 264
    step_x = 22
    step_y = 22
    radius = 1.3

    anchor_x = grid_right
    anchor_y = grid_top
    diag = math.hypot(grid_right - grid_left, grid_bottom - grid_top)

    for gx in range(grid_left, grid_right + 1, step_x):
        for gy in range(grid_top, grid_bottom + 1, step_y):
            d = math.hypot(gx - anchor_x, gy - anchor_y) / diag
            falloff = max(0.0, 1.0 - d ** 1.35)
            alpha = int(155 * falloff)
            if alpha < 12:
                continue
            color = (*COBRE, alpha)
            cx, cy = gx * scale, gy * scale
            r = radius * scale
            od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)

    over = over.resize((WIDTH, HEIGHT), Image.LANCZOS)
    img.paste(over, (0, 0), over)


def _draw_baseline_rule(img: Image.Image) -> None:
    """A single thin rule beneath the line-field. The discipline that holds the
    composition together — invisible until you look for it. Stops short of the
    canvas edge: a museum vitrine never touches its own glass."""
    od = ImageDraw.Draw(img, "RGBA")
    y = 286
    od.line([(72, y), (WIDTH - 72, y)], fill=(*VERDE_CLARO, 60), width=1)


def build() -> Path:
    img = Image.new("RGB", (WIDTH, HEIGHT), VERDE_ESCURO)
    _paint_field(img)
    _draw_dot_grid(img)
    _draw_quiet_wave(img)
    _draw_line_field(img)
    _draw_baseline_rule(img)

    out = Path(__file__).resolve().parents[1] / "hero.png"
    img.save(out, format="PNG", optimize=True)
    return out


if __name__ == "__main__":
    out = build()
    print(f"wrote {out} ({out.stat().st_size / 1024:.1f} KB)")
