# iOS Release Quality Toolkit

[![CI](https://github.com/Kofiloski/ios-release-quality-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/Kofiloski/ios-release-quality-toolkit/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A skills-only plugin for finding likely App Store release risks, repairing XCUITest testability failures, and checking iOS UI through native Xcode Simulator tools or reproducible automation.

The toolkit packages three focused workflows:

- **App Store Review Risk** — fetch Apple's current guidelines and latest update notice, then inspect an Xcode repository or PR for privacy, entitlements, StoreKit, account deletion, metadata, notarization, and other likely Apple review risks. Reports identify the policy revision, retrieval date, and sources; offline reviews disclose what still needs verification.
- **iOS UI Testability Contract** — diagnose `element not found`, wrong-element-type, accessibility-identifier collision, and nondeterministic launch-route failures in SwiftUI and UIKit.
- **iOS AI UI Check** — use Xcode 27 or later's native agent tools for focused local Simulator interaction, or add/debug provider-agnostic CI checks with screenshots, video, logs, `.xcresult`, an artifact manifest, and a managed PR summary. Local exploration uses the evidence available from its tools; repeatable regression coverage stays in app-owned tests and scenarios.

Native checks use Xcode tools already exposed to the agent. For external agents, Apple's [MCP setup](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode) requires opening the project in Xcode, allowing external agents in Intelligence settings, and connecting through `xcrun mcpbridge`. The toolkit does not configure an MCP server during installation. If native controls are unavailable, the skills use existing app-local automation and report any verification gap.

## Install from GitHub

Add this repository as a Codex plugin marketplace:

```bash
codex plugin marketplace add Kofiloski/ios-release-quality-toolkit --ref v0.2.1
```

Then install **iOS Release Quality Toolkit** from the plugin directory. The command above pins the reviewed `v0.2.1` release; replace it deliberately when adopting a newer version.

Validate a checkout without installing dependencies:

```bash
python3 scripts/check-toolkit.py
python3 -m unittest discover -s tests -v
```

Maintainers publish a version by pushing its exact `vX.Y.Z` tag. The tag workflow validates the plugin and creates the GitHub release with the built-in repository token, so no personal GitHub API or organization OAuth scope is required.

## Why The Projects Publish Differently

The toolkit presents all three projects as agent skills, but their executable delivery paths are different:

- `app-store-review-risk` and `ios-ui-testability-contract` include Python CLIs, so their release workflows publish attested packages to PyPI in addition to GitHub releases. This gives agents a short `uvx` path for one-off execution and users a clean `pipx` path for persistent installation; GitHub remains canonical for the skills and source.
- `ios-ai-ui-check` is a GitHub Action and reusable workflow. A versioned GitHub release tag is its executable distribution: callers run `Kofiloski/ios-ai-ui-check@v0.4.0` or the matching reusable workflow directly from that ref. Its repository also publishes the installable Agent Skill. The toolkit embeds that guidance, not another copy of the action runtime.

## Ask naturally

The skill descriptions are written to trigger from concrete problems, including:

- "Will Apple reject this build?"
- "Check this PR's privacy manifest and StoreKit risks."
- "XCUITest can see the button, but element lookup fails."
- "The accessibility identifier resolves to a VStack instead of the TextField."
- "Add a deterministic iOS Simulator check to this pull request."
- "Use Xcode's native tools to tap through this flow and capture the result."
- "Review this release against Apple's latest guideline changes."
- "Why did the AI UI planner reject this scenario?"

## Trust boundary

The scanner workflows run locally and do not upload repository contents. Policy reviews retrieve public Apple guidance. Native UI checks use the agent's existing Xcode connection and permissions. The `ios-ai-ui-check` reusable action is provider-agnostic; only an app-owned planner command can choose an external model provider and decide what context it receives. Review all generated changes, workflows, prompts, artifacts, and third-party credentials before use.

The tools provide engineering evidence, not a guarantee of App Store approval, accessibility compliance, or defect-free software.

## Canonical projects

- [app-store-review-risk](https://github.com/Kofiloski/app-store-review-risk)
- [ios-ui-testability-contract-skill](https://github.com/Kofiloski/ios-ui-testability-contract-skill)
- [ios-ai-ui-check](https://github.com/Kofiloski/ios-ai-ui-check)
- [Toolkit overview and policies](https://kofiloski.com/Tools)
