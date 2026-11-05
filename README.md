# iOS Release Quality Toolkit

[![CI](https://github.com/Kofiloski/ios-release-quality-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/Kofiloski/ios-release-quality-toolkit/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Three agent skills for reviewing Apple release risks, repairing XCUITest failures, and checking iOS Simulator UI.

| Skill | Use it to |
| --- | --- |
| [App Store Review Risk](https://github.com/Kofiloski/app-store-review-risk) | Review likely submission risks against current Apple guidance. |
| [UI Testability Contract](https://github.com/Kofiloski/ios-ui-testability-contract-skill) | Fix element lookup, identifier, and deterministic launch failures. |
| [iOS AI UI Check](https://github.com/Kofiloski/ios-ai-ui-check) | Run focused native checks or app-owned Simulator scenarios in CI. |

## Install

Add the release-pinned Codex plugin marketplace:

```bash
codex plugin marketplace add Kofiloski/ios-release-quality-toolkit --ref v0.2.3
```

Then install **iOS Release Quality Toolkit** from the plugin directory. Individual skills are also available from their canonical repositories for compatible coding agents.

## Ask naturally

- "Review this iOS app for likely App Store rejection risks."
- "Fix this XCUITest element-not-found failure."
- "Verify this UI flow locally and preserve it as a regression test."
- "Use Anthropic with claude-sonnet-4-6 at high effort for UI planning."

UI Check v0.6.0 supports explicit provider, model, and effort settings. Existing app integrations need a scaffold refresh and updated action pin; installing the toolkit does not update app scripts or change the host coding-agent session.

## Requirements and limits

This is a skills-only bundle. It does not install scanners, Xcode connections, or third-party inspectors. The local baseline uses Xcode/XCTest and Apple's command-line tools. Deterministic scenarios and local scanners need no model key; optional AI planning uses the provider chosen by the app repository.

The skills produce engineering evidence, not a guarantee of App Store approval or complete UI coverage. [Setup, planner configuration, privacy, and delivery channels](docs/usage.md).

## Documentation

- [Using the toolkit](docs/usage.md): native setup, planner choices, example requests, and trust boundaries.
- [Skill maintenance](docs/skill-maintenance.md): canonical bundles, validation, and publication.
- [Ice Cubes evaluation](docs/simulator-test-app.md) and [popular-app status](docs/popular-app-benchmarks.md): actual evidence and remaining gaps.

MIT licensed. [Website and policies](https://kofiloski.com/Tools) · [Agent discovery](llms.txt) · [Citation metadata](CITATION.cff).
