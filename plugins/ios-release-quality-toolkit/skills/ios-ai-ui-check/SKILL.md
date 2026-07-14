---
name: ios-ai-ui-check
description: Add, operate, or debug reproducible iOS Simulator UI checks in GitHub Actions with ios-ai-ui-check. Use when someone asks for AI-planned or deterministic XCUITest checks from a plain-English goal, wants video/screenshots/logs/xcresult artifacts and a PR summary, needs to scaffold an app-owned runner or scenario, or is troubleshooting planner validation, Simulator, runner, artifact-manifest, or pull-request-comment failures. Keep app launch state, fixtures, accessibility identifiers, UI interactions, and assertions in the app repository; keep the reusable action provider-agnostic.
---

# iOS AI UI Check

Integrate the public `Kofiloski/ios-ai-ui-check` action without hiding app-specific test truth inside the reusable workflow.

## Workflow

1. Read the target repository's instructions and CI setup. Identify the `.xcodeproj`, shared scheme, UI-test target, supported Simulator destination, and current launch/testing helpers.
2. Choose the least-variable mode that satisfies the request:
   - Prefer a checked-in scenario for required or security-sensitive CI.
   - Use a planner goal when exploratory coverage is useful and the app repo can explicitly control the context sent to its chosen provider.
3. Read `references/adoption.md` before scaffolding or editing a workflow.
4. Pin the public action to a release tag or commit SHA. Do not track `main` in stable CI.
5. Use the upstream scaffold for a new integration. Run its dry-run first, review the proposed files, then generate them only within the target app repo.
6. Review the generated app-owned contract before running it:
   - deterministic launch arguments and environment values
   - safe fixtures, mocks, or test accounts
   - stable accessibility identifiers on the actual controls
   - focused assertions that prove the requested behavior
   - planner context that contains no secrets
7. Run the checked-in scenario locally before enabling a PR workflow. Treat Simulator availability, Xcode version, and shared-scheme failures as setup problems rather than planner problems.
8. Inspect `summary.md`, `manifest.json`, logs, screenshots, video, and `.xcresult` together. Do not report success from a status dot when the evidence contradicts it.
9. Keep fixes at the correct boundary:
   - reusable orchestration or artifact-contract defect -> fix `ios-ai-ui-check`
   - element lookup, wrong element type, identifier collision, or unreachable route -> use `$ios-ui-testability-contract`
   - app launch, data, interaction, or assertion logic -> fix the app-owned runner

## Guardrails

- Do not move app-specific launch, seeding, UI interaction, or assertions into the reusable action.
- Do not add a hard-coded model provider to the action. Only the app-owned planner command may choose a provider.
- Never pass secrets through prompts, planner context, logs, scenarios, screenshots, or artifacts.
- Prefer `pull_request` when compiling and running pull-request code. Do not switch to `pull_request_target` to gain secret access.
- Start with manual or label-triggered runs. Make the check required only after launch state and identifiers are deterministic.
- Do not promise visual correctness unless the app-owned scenario contains an explicit, reviewable assertion for it.

## Completion evidence

Report:

- selected deterministic or planner mode and why
- action ref and Simulator/Xcode assumptions
- app-owned files added or changed
- exact local or CI command run
- artifact paths inspected
- any remaining app-specific contract or credential work
