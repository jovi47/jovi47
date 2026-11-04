# GitHub profile README

Updated: 2026-11-03 UTC. The current revision is an English personal introduction, with five-plus years of experience and Elixir first. The owner requested a lighter profile focused on projects, interests and a technology section resembling the portfolio. Work-history sections, employer metrics and CV-style skill bullets are removed from the visible README. No career fact is retracted or changed in the CVs or LinkedIn.

## Content and sources

The short introduction reuses the approved portfolio About text: curiosity about technology, learning by building, LEGO, web/3D and applied AI/RAG/agents. Systems are introduced briefly: ASC-Hub, HorAgora and the personal portfolio. No new hobby, seniority, language fluency or result is invented. Public contact remains ojoaovsousa@gmail.com and the portfolio uses its published English route.

Project links use their existing brands as the clickable target: the ASC symbol opens the consultancy website, HorAgora retains its linked wordmark, and the personal portfolio uses the pixel-style ojoaovsousa wordmark from its published header. The separate Consultancy website link and generic portfolio cube are removed. Both new wordmarks contain the exact Pixelify regular glyph outlines with -1px tracking, local light/dark fills, accessible link names and no embedded font or external dependencies.

The Brazil flag, location/availability and the existing Portfolio/LinkedIn/Email links appear immediately below the professional role, with natural wrapping and no duplicate footer block.

The name heading preserves the56px inline GIF and reduced-motion PNG fallback from PR4. The real account photograph and portfolio scene are outside this revision.

## Technology presentation

The portfolio's existing icon/name strip is the visual reference: two continuous rows moving in opposite directions, with the Elixir ecosystem first. The README keeps its27names and26source icons, including the Phoenix symbol reused for LiveView. Self-contained light/dark SVGs embed the existing paths with collision-safe local IDs; no JavaScript, external image reference, font request or dependency is needed. Each row repeats seamlessly, with56s/62s CSS animations,29px icons and15px labels. `python3 scripts/build-technology-marquee.py` regenerates both assets and their manifest entries from the native static list.

The README image requests840×108pixels; the embedded SVG root uses `width="100%"`, `height="108"` and no root `viewBox` so its viewport follows the image width while retaining native icon/label coordinates. GitHub's actual responsive image sizing must be checked in its renderer: the earlier fixed-width SVG was horizontally compressed on narrow screens. CSS `prefers-reduced-motion` stops both rows. All names remain available in the image alt/SVG title and in the original naturally wrapping native list under “All technologies (static list)”; the static list also covers image/animation failures. GitHub's Markdown sanitizer and image proxy remain outside this repository's control.

Original source SVGs, paths and license files remain unchanged. [Media sizes, hashes, sources and licenses](readme-assets.json), [Devicon MIT](../images/LICENSE.txt) and [portfolio technology notices](../images/TECHNOLOGY-LICENSES.txt) record provenance, Simple Icons CC0, Git CC BY3.0 and brand boundaries. Project/employer marks do not imply endorsement. Previously added employer identifiers are retained in the source inventory but are not shown in the personal README.

## Verification and publication boundary

Verification covers native GitHub Markdown rendering, all image paths, exact source hashes, SVG safety, visible labels, header/body structure and local whitespace. Browser review covers wrapping, narrow screens and the live profile after publication. No new cosmetic automated test or remote development test pipeline is required. Preparing this branch is not evidence of publication; canonical Obsidian notes record actual PR/main/profile state once observed.

The base contains no GitHub Actions workflow. One new internal worktree/branch/PR is used because the preceding alignment PR was already merged. DraftPR1 remains untouched. This change does not deploy the portfolio or change Search Console, account authentication or privacy settings.

## Costs

Static copy, local wordmark outline conversion and self-contained animated SVG composition only; no paid image generation, provider, dependency, subscription, recurring job or remote test pipeline. The four new SVGs add142,308source bytes across both themes. Existing GIF media are unchanged. Transfer scenario remains uncached profile reads×bytes actually fetched for the chosen images, with cache/proxy behavior determining real traffic. Traffic, tariffs and monthly bill remain unknown. Source asset sizes and the added SVG/license inventory are recorded in the manifest; the canonical portfolio costs note records the final measured file delta.

Canonical personal copy, preferences, provenance and publication evidence remain in Obsidian portfolio/github-profile.md. This document describes the repository revision and its real publication boundary.

This branch combines the three separately scoped README requests for visual review only. It does not change main or the public profile. Both native technology disclosures support keyboard hide/show; reduced motion disables both animation belts.
