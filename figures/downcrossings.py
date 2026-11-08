#!/usr/bin/env python3
"""Generate the down-crossing figure (Chapter 1, "Down-crossing approximations").

Simulates a reflected Brownian path X = |B| started at 0 and marks the stopping times used to
count down-crossings from level epsilon to level 0:

    sigma_0 = 0,          tau_0 = inf{t : X_t = eps},
    sigma_n = inf{t > tau_{n-1} : X_t = 0},
    tau_n   = inf{t > sigma_n   : X_t = eps}.

The random seed is chosen deterministically (the first seed whose path shows
exactly two completed down-crossings, nicely spaced), so the output is
reproducible.

Usage:
    python3 figures/downcrossings.py            # writes figures/downcrossings.pdf
    python3 figures/downcrossings.py out.png    # any format matplotlib supports
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

N_STEPS = 2000  # time steps on [0, 1]
EPS = 0.35  # the level epsilon
N_DOWNCROSSINGS = 2  # completed down-crossings shown on [0, 1]
MIN_GAP = 0.07  # minimal spacing between consecutive marked times
CLIMB_STEPS = 25  # steps before each tau excluded from the near-miss check
MAX_SEED = 500_000


def first_index(x, start, condition):
    """First index i >= start with condition(x[i]) true, or None."""
    hits = np.flatnonzero(condition(x[start:]))
    return start + hits[0] if hits.size else None


def stopping_times(x):
    """Return (taus, sigmas) as index lists, with sigma_0 = 0."""
    taus, sigmas = [], [0]
    i = 0
    while True:
        tau = first_index(x, i, lambda v: v >= EPS)
        if tau is None:
            return taus, sigmas
        taus.append(tau)
        sigma = first_index(x, tau, lambda v: v <= 0)
        if sigma is None:
            return taus, sigmas
        sigmas.append(sigma)
        i = sigma


def acceptable(t, x, taus, sigmas):
    """Keep paths that make a readable figure."""
    if len(sigmas) != N_DOWNCROSSINGS + 1 or len(taus) != N_DOWNCROSSINGS:
        return False  # exactly d_eps(1) = N_DOWNCROSSINGS, no extra tau
    marks = sorted(t[taus + sigmas])
    if t[taus[0]] < 0.2 or marks[-1] > 0.85 or np.min(np.diff(marks)) < MIN_GAP:
        return False
    # each excursion clearly overshoots eps before coming back down to 0
    for tau, sigma in zip(taus, sigmas[1:]):
        if x[tau:sigma].max() < 1.4 * EPS:
            return False
    # before each tau the path stays clearly below eps (no visual near-misses)
    # (the last CLIMB_STEPS before tau are the final climb and are not checked)
    for sigma, tau in zip(sigmas, taus):
        if np.max(x[sigma:tau - CLIMB_STEPS], initial=0.0) > 0.8 * EPS:
            return False
    # the path does not wander up to eps again after the last down-crossing
    if x[sigmas[-1]:].max() > 0.8 * EPS:
        return False
    return x.max() < 2.2 * EPS


def simulate():
    t = np.linspace(0.0, 1.0, N_STEPS + 1)
    dt = t[1] - t[0]
    for seed in range(MAX_SEED):
        rng = np.random.default_rng(seed)
        b = np.concatenate([[0.0], np.cumsum(rng.normal(0, np.sqrt(dt), N_STEPS))])
        x = np.abs(b)
        # B changes sign between grid points: the path hits 0 there
        x[1:][np.sign(b[1:]) != np.sign(b[:-1])] = 0.0
        taus, sigmas = stopping_times(x)
        if acceptable(t, x, taus, sigmas):
            return seed, t, x, taus, sigmas
    raise RuntimeError("no acceptable path found; relax the criteria")


def plot(t, x, taus, sigmas, out):
    plt.rcParams.update({"mathtext.fontset": "cm", "font.family": "serif", "font.size": 11})
    fig, ax = plt.subplots(figsize=(6.0, 3.0))

    ax.plot(t, x, color="black", linewidth=0.8)
    ax.axhline(EPS, color="0.5", linewidth=0.6)
    ax.axhline(0, color="black", linewidth=0.8)

    for n, i in enumerate(taus):
        ax.plot([t[i], t[i]], [0, EPS], linestyle="--", color="black", linewidth=0.8)
        ax.annotate(rf"$\tau_{n}^\varepsilon$", (t[i], 0), xytext=(0, -14),
                    textcoords="offset points", ha="center", va="top")
    ax.annotate(r"$\sigma_0^\varepsilon = 0$", (0, 0), xytext=(-6, 0),
                textcoords="offset points", ha="right", va="center")
    for n, i in enumerate(sigmas[1:], start=1):
        ax.plot(t[i], 0, "o", color="black", markersize=4, zorder=3)
        ax.annotate(rf"$\sigma_{n}^\varepsilon$", (t[i], 0), xytext=(0, -14),
                    textcoords="offset points", ha="center", va="top")

    ax.set_yticks([EPS], [r"$\varepsilon$"])
    ax.set_xticks([])
    ax.set_xlim(0, 1.03)
    ax.set_ylim(-0.05 * EPS, 2.3 * EPS)
    ax.set_xlabel(r"$t$", loc="right")
    ax.set_ylabel(r"$X_t$", loc="top", rotation=0)
    for side in ("top", "right", "bottom"):
        ax.spines[side].set_visible(False)

    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")


def main():
    default = Path(__file__).with_name("downcrossings.pdf")
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    seed, t, x, taus, sigmas = simulate()
    plot(t, x, taus, sigmas, out)
    print(f"seed {seed}: wrote {out}")


if __name__ == "__main__":
    main()
