# GitHub profile README

Updated: 2026-11-03 UTC. The current revision is an English personal introduction, with five-plus years of experience and Elixir first. The owner requested a lighter profile focused on projects, interests and a technology section resembling the portfolio. Work-history sections, employer metrics and CV-style skill bullets are removed from the visible README. No career fact is retracted or changed in the CVs or LinkedIn.

## Content and sources

The short introduction reuses the approved portfolio About text: curiosity about technology, learning by building, LEGO, web/3D and applied AI/RAG/agents. Systems are introduced briefly: ASC-Hub, HorAgora and the personal portfolio. No new hobby, seniority, language fluency or result is invented. Public contact remains ojoaovsousa@gmail.com and the portfolio uses its published English route.

The name heading preserves the56px inline GIF and reduced-motion PNG fallback from PR4. The real account photograph and portfolio scene are outside this revision.

## Technology presentation

The portfolio's existing icon/name strip is the visual reference: two continuous rows moving in opposite directions, with the Elixir ecosystem first. The README keeps its27names and26source icons, including the Phoenix symbol reused for LiveView. Self-contained light/dark SVGs embed the existing paths with collision-safe local IDs; no JavaScript, external image reference, font request or dependency is needed. Each row repeats seamlessly, with56s/62s CSS animations,29px icons and15px labels. `python3 scripts/build-technology-marquee.py` regenerates both assets and their manifest entries from the native static list.

The image has an explicit840×108pixel box and no root `viewBox`, allowing a narrower viewport to clip the horizontal rows while preserving icon/label size. GitHub's actual responsive image sizing must be checked in its renderer. CSS `prefers-reduced-motion` stops both rows. All names remain available in the image alt/SVG title and in the original naturally wrapping native list under “All technologies (static list)”; the static list also covers image/animation failures. GitHub's Markdown sanitizer and image proxy remain outside this repository's control.

Original source SVGs, paths and license files remain unchanged. [Media sizes, hashes, sources and licenses](readme-assets.json), [Devicon MIT](../images/LICENSE.txt) and [portfolio technology notices](../images/TECHNOLOGY-LICENSES.txt) record provenance, Simple Icons CC0, Git CC BY3.0 and brand boundaries. Project/employer marks do not imply endorsement. Previously added employer identifiers are retained in the source inventory but are not shown in the personal README.

## Verification and publication boundary

`python3 scripts/build-technology-marquee.py --check` checks deterministic output and manifest hashes, original embedded path geometry,27labels, unique IDs, resolved local SVG references and absence of scripts/external images. Local review also checks existing asset hashes, README paths and whitespace. Browser review must cover motion, seamless looping, both themes, reduced motion, native static-list wrapping and320–430px/tablet/desktop image sizing in GitHub's renderer. No remote development test pipeline is required. Preparing this branch is not evidence of publication; canonical Obsidian notes record actual PR/main/profile state once observed.

The base contains no GitHub Actions workflow. One new internal worktree/branch/PR is used because the preceding alignment PR was already merged. DraftPR1 remains untouched. This change does not deploy the portfolio or change Search Console, account authentication or privacy settings.

## Costs

The two generated SVG variants add136,720bytes to the repository; one selected theme variant is68,360bytes per uncached fetch. Generation uses only the Python standard library and existing public artwork; no provider, dependency, subscription, recurring job or remote test pipeline is added. Existing GIF media are unchanged. Transfer scenario is uncached profile reads×(selected marquee bytes+other images actually fetched, including static-list icons when requested); cache/proxy behavior determines real traffic. Traffic, tariffs and monthly bill remain unknown. Exact media sizes/hashes are in the manifest; canonical portfolio costs records the final measured delivery delta.

Canonical personal copy, preferences, provenance and publication evidence remain in Obsidian portfolio/github-profile.md. This document describes the repository revision and its real publication boundary.

The animated strip is inside an initially open native disclosure, so readers can hide the continuous movement without scripts; the complete static list remains in its separate disclosure.
