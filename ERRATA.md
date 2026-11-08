# Errata: corrections to the 2018 version

This file lists the changes made in 2026 to the mathematical content of the thesis
submitted in 2018. Theorem numbers refer to the corrected version.

## Chapter 1 — Local times of semimartingales
- Normalisation fixed (Revuz–Yor convention): local time L^a is the increasing process
  associated with (x−a)^+; |X−a| = |X_0−a| + ∫ sgn dX + L^a (the 2018 text had a spurious
  factor 2 in front of the stochastic integral, repeated in five places).
- Tanaka's formula for (X−a)^-: missing minus sign in front of ∫ 1_{X≤a} dX.
- Theorem 1.1: Doob's inequality constant misplaced; f_n''(X_t) → f_n''(X_s); inconsistent
  factors of 1/2 in K^n; removed an invalid identity using f'' for a merely convex f;
  localisation argument rewritten.
- Lemma 1.10 (measurability): predictable σ-field defined with F_s (not F_a); proof of the
  monotone-class step rewritten (measurable choice of subsequence).
- Theorem 1.11 (stochastic Fubini): proof rewritten.
- Occupation times formula: proof completed (identification of measures).
- Theorem 1.14 (joint continuity): stated for local martingales, proof no longer uses a drift;
  integrals against dx (not d⟨X⟩) after the occupation formula; constants corrected.
- Theorem 1.16 (bicontinuity in t, càdlàg in a): proof completed (bound for the martingale part).
- Corollary 1.18: proof replaced by the direct argument (occupation formula + right
  continuity); the previous proof had wrong limits (f''_ε → δ_a) and was incomplete.
- Down-crossings: added hypothesis X_0 = 0; definition of S^p moved before use.
- Symmetric local time: sign corrected, L̂^a = L^a − ∫ 1_{X=a} dX = (L^a + L^{a−})/2.
- Example X = c_+B^+ − c_−B^−: corrected computation; L^0(X) = c_+L^0(B), L̂^0(X) = (c_+ + c_−)/2 L^0(B).
- Symmetric Itô–Tanaka formula: proof previously used the non-symmetric local time.
- Example 1.15 (after Theorem 1.14) retitled "Reflected Brownian motion" (it is about |B|).
- Added citations: Durrett (1996), Revuz–Yor (1999), Tanaka (1963), Meyer (1976).

## Chapter 2 — SDEs involving the local time at zero
- Setting made precise: L is the right local time; α locally bounded; definitions of
  solution, uniqueness in law and pathwise uniqueness added.
- Skorokhod's lemma restated in the standard form (y(0) ≥ 0, l = sup(−y) ∨ 0), needed
  because |X| starts at |x|; existence proof added; "x_i only increases" → "l_i".
- Lévy's theorem: S_t defined; sup over s ≤ t (was ∫_0^t inside the sup).
- Proposition on reflected BM: missing "= 0" in condition (iii); proof fixed.
- Uniqueness in law: |X| is a reflected (not standard) BM; L = ∫ dL̂/(1−α) derived from the
  jump formula; integrability of L justified; passage from one-dimensional marginals to the
  full law now uses regular conditional distributions (Stroock–Varadhan argument).
- Local time of X¹ ∨ X²: the 2018 proof (Lipschitz map Z, down-crossings) was not valid.
  Replaced by Lemmas 2.6–2.8 and a complete proof that the maximum of two solutions is a
  solution (Tanaka identification, occupation formula with weights, portmanteau bounds for
  right and left local times, jump formula).
- "iff" proposition replaced by what is actually used and proved.
- Remark on α ≤ 1/2: the 2018 text said the hypothesis was "almost useless"; it is in fact
  necessary (left local time L^{0−} = ∫(1−2α)dL must be increasing); proof of non-existence
  for α > 1/2 added.
- Constant α: identified as skew BM with β = α/(1−α) ∈ ]−1, 1].
- General σ, b: removed the invalid "domain invariance" justification; h'' computed;
  local time of Y = h(X) computed (L(Y) = L(X)/σ(0)); new drift composed with h^{-1};
  the transformed equation now uses L(Y), not L̂; Girsanov step made explicit.
- Added citations: Le Gall (1983), Perkins (1982), Revuz–Yor, Karatzas–Shreve.

## Chapter 3 — SDEs involving the local times of the unknown process
- Equation (3.1) now uses symmetric local times, consistently with the rest of the chapter;
  (3.2) has ∫_0^t (not ∫_R) and uses φ; (3.3) uses β (the text had ν = αδ_0).
- Lemma 3.1: conclusion is L^0(X) = 0 for the right local time (was "L̂^{0+}"); proof uses
  right continuity in a (not continuity of symmetric local times).
- Conditions (A), (B) stated once; (B) requires f bounded (used in the proof); examples added.
- Corollary 3.2, case (B): the approximation of f by C¹ functions was not justified for f
  with jumps; replaced by a direct argument via the Stieltjes measure of f, Fatou and the
  occupation formula; mixed ∫_0^s / ∫_0^t, f(s, X) and a misplaced constant fixed.
- Theorem 3.4: pathwise uniqueness proof via the maximum of two solutions written out.
- Comparison theorem 3.6: the proof bounded (X¹−X²)^+ with the indicator of {X¹<X²};
  it now bounds (X²−X¹)^+; hypotheses (A) or (B) (was "A) and B)").
- Theorem 3.7: coefficients made time-homogeneous (the statement mixed σ_n(t,x) with L¹
  conditions in x only); σ(t, X^n) → σ(X); "for all t" → "for all M".
- Le Gall's lemma: normalisation f → 1 as x → −∞ (was +∞); proof added.
- Proposition 3.9: F_μ → F_ν; the symmetric derivative written correctly (the text had
  (f+f)/2 (X_s^-)); converse direction proved (computation of the atoms of ν).
- Existence/uniqueness for (3.7): explained why the transformed coefficient satisfies (B).
- Limit theorem: |μ_n| → |ν_n|; missing ν(da) in the limit equation (three places);
  f_n defined with ν_n and h_n with φ_n; triangle inequality for the initial values fixed;
  uniform bounds on f_{ν_n} justified.
- Remark on ν_n → Aδ_0: limit coefficient identified as tanh(A).
- Scaling corollary: Rosenkrantz (1975) reference added; requires φ ≡ 1 (the statement had a general φ); proof of the scaling of
  local times added; missing parenthesis in the formula for β.
- Comparison theorem for measures: inequality ν ≥ μ was reversed in the proof; the
  approximation now replaces each atom c by artanh(c) before mollifying (mollifying ν
  directly gives the wrong limit, by the preceding remark); first step uses Theorem 3.4
  (not the limit theorem).

## Chapter 4 — Parabolic PDEs
- Laplacian was written as sum of ∂²u_i/∂x_i² (components of u); now Σ ∂²u/∂x_i².
- ℂ^{1,2} (complex numbers) → C^{1,2}.
- Heat local-martingale proof: claimed ∂u/∂t + ½Δu = 0; correct is −∂u/∂t + ½Δu = 0.
- Feynman–Kac "v smooth ⇒ solution": integrand had +∂v/∂t; correct is −∂v/∂t + cv + ½Δv.
- FK boundary proof: "|c| ≤ " missing M; now gives uniform bound ‖f‖(e^{Mt}−1).
- Differentiation lemma was circular (assumed ∂u/∂x_i to conclude it); restated with w(x)=∫∂_iK g dm.
- Smoothness of heat solution: added locally uniform integrable dominating function.
- "v smooth ⇒ solution": made the "positive probability" argument precise (start at x0, horizon t0).
- Candidate solution renamed ν → v (ν is a measure in Chapter 3).
- Unbounded-f theorem had no subject; "no uniqueness" sentence replaced by a remark (Tychonoff, growth classes).
- Inhomogeneous equation was announced but not treated; now said explicitly.
- Hölder-smoothness theorem stated without proof; now cites Durrett and Friedman.
- Added attribution to Durrett and a closing section linking to the transmission problem of Chapter 5.

## Chapter 5 — Skew Brownian motion
- SBM now defined consistently as X = x + W + β L̂⁰(X) with the symmetric local time (original mixed L⁰, α and β).
- Existence/uniqueness now referenced (Theorem 3.10 with ν = βδ₀; Harrison–Shepp); scale-function remark added.
- Random-flipping construction: τ_t lacked "inf" and used L(X) before X was defined; ξ, F^β, (C,𝒞,ℝ) undefined. Rewritten with a measurable enumeration of excursion intervals.
- Lemma |X| ~ |W|: now proved (Itô–Tanaka + Skorokhod), at process level; remark had max over "0 ≤ 0 ≤ t".
- Flip lemma: conditioning argument rewritten; "proceeding similarly on R₊*" should have been R₋*.
- Joint law: "(4) with μ = 0" leftover removed; proof rewritten via first-passage convolution; new lemma for the BM joint law (Lévy + reflection principle).
- Transition density was p(t,x,y) + β sgn(y) p(t,−x,y) — wrong for y < 0 or x < 0. Correct: p_t(y−x) + β sgn(y) p_t(|x|+|y|) (checked numerically via Chapman–Kolmogorov).
- PDE: regularity class fixed; added a proof that E_x f(X_t) solves the transmission problem.
- Transmission derivation: missing ½ in front of ∫f″, inconsistent β/(1+β) vs β/(1−β), garbled Itô–Tanaka line. Redone: coefficient of L̂ is ½[(1+β)f′(0+) − (1−β)f′(0−)].
- Divergence form: Hilbert space is L²(ℝ, k dx), not L²(dx); Dirichlet-form remark made precise.
- Citations added: Itô–McKean, Walsh, Harrison–Shepp, Portenko, Étoré–Martinez (2012, the likely source of Section 5.1).

## Other changes (not mathematical)
- Source split into `main.tex`, `preamble.tex`, `frontmatter/` and one file per chapter;
  bibliography moved to `references.bib` (natbib, `plainnat`).
- The 2018 source had about 180 LaTeX errors (missing theorem arguments, undefined
  macros, stray environments); it now compiles without errors.
- Theorem-like environments use `amsthm` with a single counter per chapter.
- The down-crossings figure is generated by `figures/downcrossings.py` instead of being a
  hand-made image.
- New title page, abstract and introduction; acknowledgements and the whole text proofread.
- One-sided layout, suited to reading on screen.
