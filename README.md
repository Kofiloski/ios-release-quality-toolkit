# iOS Release Quality Toolkit

[![CI](https://github.com/Kofiloski/ios-release-quality-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/Kofiloski/ios-release-quality-toolkit/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A skills-only plugin for finding likely App Store release risks, repairing XCUITest testability failures, and adding evidence-rich iOS Simulator checks.

The toolkit packages three focused workflows:

- **App Store Review Risk** — inspect an Xcode repository or PR for privacy manifests, permission strings, entitlements, StoreKit, account deletion, metadata, notarization, and other likely Apple review risks.
- **iOS UI Testability Contract** — diagnose `element not found`, wrong-element-type, accessibility-identifier collision, and nondeterministic launch-route failures in SwiftUI and UIKit.
- **iOS AI UI Check** — add or debug provider-agnostic, reproducible Simulator checks with screenshots, video, logs, `.xcresult`, an artifact manifest, and a managed PR summary.

## Install from GitHub

Add this repository as a Codex plugin marketplace:

```bash
codex plugin marketplace add Kofiloski/ios-release-quality-toolkit --ref v0.1.1
```

Then install **iOS Release Quality Toolkit** from the plugin directory. The command above pins the reviewed `v0.1.1` release; replace it deliberately when adopting a newer version.

Validate a checkout without installing dependencies:

```bash
python3 scripts/check-toolkit.py
python3 -m unittest discover -s tests -v
```

Maintainers publish a version by pushing its exact `vX.Y.Z` tag. The tag workflow validates the plugin and creates the GitHub release with the built-in repository token, so no personal GitHub API or organization OAuth scope is required.

## Why The Projects Publish Differently

The toolkit presents all three projects as agent skills, but their executable delivery paths are different:

- `app-store-review-risk` and `ios-ui-testability-contract` include Python CLIs, so their release workflows publish attested packages to PyPI in addition to GitHub releases. This gives agents a short `uvx` path for one-off execution and users a clean `pipx` path for persistent installation; GitHub remains canonical for the skills and source.
- `ios-ai-ui-check` is a GitHub Action and reusable workflow. A versioned GitHub release tag is its executable distribution: callers run `Kofiloski/ios-ai-ui-check@v0.3.0` or the matching reusable workflow directly from that ref. The toolkit bundles the agent-facing adoption and debugging guidance, not another copy of the action runtime.

## Ask naturally

The skill descriptions are written to trigger from concrete problems, including:

- "Will Apple reject this build?"
- "Check this PR's privacy manifest and StoreKit risks."
- "XCUITest can see the button, but element lookup fails."
- "The accessibility identifier resolves to a VStack instead of the TextField."
- "Add a deterministic iOS Simulator check to this pull request."
- "Why did the AI UI planner reject this scenario?"

## Trust boundary

The bundled scanners run locally and do not upload repository contents. The `ios-ai-ui-check` reusable action is provider-agnostic; only an app-owned planner command can choose an external model provider and decide what context it receives. Review all generated changes, workflows, prompts, artifacts, and third-party credentials before use.

The tools provide engineering evidence, not a guarantee of App Store approval, accessibility compliance, or defect-free software.

## Canonical projects

- [app-store-review-risk](https://github.com/Kofiloski/app-store-review-risk)
- [ios-ui-testability-contract-skill](https://github.com/Kofiloski/ios-ui-testability-contract-skill)
- [ios-ai-ui-check](https://github.com/Kofiloski/ios-ai-ui-check)
- [Toolkit overview and policies](https://kofiloski.com/Tools)
