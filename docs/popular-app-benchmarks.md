---
summary: Local validation status and public benchmark preparation for Firefox, DuckDuckGo, and Proton Pass.
read_when:
  - Selecting popular open-source iOS apps for public evaluation forks
  - Preparing hosted release-comparison checks for third-party apps
---

# Popular-app benchmark candidates

Status: Local bring-up started November 4, 2026. All three isolated checkouts are present. Source inventories and static review scans completed, and Proton Pass's focused password tests passed on iOS Simulator. Full-app builds and app UI checks remain unverified. No remote forks or hosted workflows have been created, and showcase publication is pending local proof. The earlier Ice Cubes results do not establish buildability or coverage for these apps.

The recommended brand shortlist is Firefox, DuckDuckGo, and Proton Pass. GitHub metadata reports that all three repositories are public, active, and allow forks. Repository stars measure developer visibility; US App Store rating counts give a separate, imperfect product-audience signal. Neither measure establishes downloads, active users, or the audience a case study would attract.

| App/source | GitHub stars | License reported by source | US App Store ratings displayed |
| --- | --- | --- | --- |
| [Firefox](https://github.com/mozilla-mobile/firefox-ios) | 13,070 | MPL-2.0 | [219K](https://apps.apple.com/us/app/firefox-fast-private-browser/id989804926) |
| [DuckDuckGo](https://github.com/duckduckgo/apple-browsers) | 270 | Apache-2.0, with a separately licensed font excluded | [2.4M](https://apps.apple.com/us/app/duckduckgo-optional-duck-ai/id663592361) |
| [Proton Pass](https://github.com/protonpass/ios-pass) | 302 | GPLv3 or later per README | [8.9K](https://apps.apple.com/us/app/proton-pass-password-manager/id6443490629) |

The initial inspected source trees were Firefox `373f4ae9a082155e5953e8595647316dae2631fd`, DuckDuckGo `838a682e32d0e300c921aae4bf8cf02a203ea5bc`, and Proton Pass `bd22de62d53815d04feeee2da91c9478e71530a0`. These are dated inspection points, not automatically selected release commits. Recheck and pin actual released versions when implementing a comparison.

## Local verification so far

The checkouts are `Firefox-SkillsTest`, `DuckDuckGo-SkillsTest`, and `ProtonPass-SkillsTest` under the owner's iOS projects directory, at the revisions above. They are shallow branch snapshots; no released comparison pair has been selected. Xcode 27.1 is selected through command-scoped `DEVELOPER_DIR`, with the dedicated iPhone 18 Pro Simulator on iOS 27.0. No external UI inspector or global convenience utility was installed.

- Launch and identifier inventories completed for all three apps. Multiapp source inventories include other products and test fixtures; they do not prove runtime identifiers or routes.
- Firefox's locked Node dependency preparation and production JavaScript resource build passed, with the upstream npm lockfile unchanged. Nimbus setup scripts were pinned and inspected but not executed; the native app still needs its remaining preparation and build.
- Static App Review scanner runs completed for Firefox and Proton Pass. The whole DuckDuckGo scan exceeded a 120-second local limit; an explicit `--submitted-target DuckDuckGo` replay completed in 55.37 seconds. These are heuristic source reports, without a live policy review or adjudication of findings.
- Proton Pass's existing `PasswordRulesTests` and `PasswordPreferencesTests` passed through the `Entities-Package` scheme: 21 tests, zero failures, with an inspected `.xcresult`. Host `swift test` first failed on an unconditional UIKit import; the library-only `Entities` scheme also lacks a test action. The successful replay used the package's iOS Simulator test scheme.
- DuckDuckGo's documented private-font removal and local external-developer configuration are prepared. Project syntax validation passed; this does not establish app buildability.
- A Proton build-only scheme excludes the upstream actions that modify every booted Simulator or install wget. Its required public Rust package was downloaded with an existing tool and matched the pinned SHA-256. The stock private UI-test target was not run. A separate public XCTest scaffold has only been previewed.
- Proton app dependency preparation remains incomplete. A bounded process sample located a wait inside Keychain credential lookup. Retrying with Xcode's supported `-packageAuthorizationProvider netrc` option began public binary downloads, then hit the local 1 GiB free-space reserve during extraction. The generated 24-pin app lockfile and both attempts were preserved; a lockfile alone is not a successful resolution or build.

The evaluation also produced a narrow identifier-scanner optimization: generated source files without either supported identifier token are skipped before lexing. Replayed Firefox and DuckDuckGo reports were identical to the original reports, while timings fell from 84.39 to 2.40 seconds and 99.70 to 4.29 seconds respectively. The scanner's 45 tests passed, including a large generated-companion regression test. Those findings informed the tooling releases published on November 5, 2026: [UI Check v0.5.0](https://github.com/Kofiloski/ios-ai-ui-check/releases/tag/v0.5.0), [Testability v0.4.3](https://github.com/Kofiloski/ios-ui-testability-contract-skill/releases/tag/v0.4.3), [App Review Risk v0.3.3](https://github.com/Kofiloski/app-store-review-risk/releases/tag/v0.3.3), and [Toolkit v0.2.2](https://github.com/Kofiloski/ios-release-quality-toolkit/releases/tag/v0.2.2).

The first explicitly approved cleanup removed four completed build-product directories (4.33 GiB measured; about 4.51 GiB observed free-space gain), preserving source and test evidence. Further cleanup requires approval of its separately enumerated paths. Run apps sequentially after making sufficient room for dependency extraction and compilation; do not infer space requirements from checkout size.

The source revisions, integration patches, commands, scan outputs, `.xcresult`, storage audit and current gaps are in the sibling `test-results/popular-ios-local/` directory outside the distributable bundle. Do not present the three apps as passing UI checks or a completed release-comparison showcase.

## Build and test feasibility

**Firefox:** the current [root README](https://github.com/mozilla-mobile/firefox-ios/blob/main/README.md) specifies Xcode 27.1. The [app README](https://github.com/mozilla-mobile/firefox-ios/blob/main/firefox-ios/README.md) describes Node/bootstrap preparation and the `Fennec` scheme. Existing unit and UI tests should be reused after inspecting the exact release's launch hooks. The checked-in GitHub UI workflow still references older Xcode/runner combinations and includes Slack reporting; do not copy or enable it wholesale in a benchmark fork. Read its `AGENTS.md`, contribution guide, bootstrap script, and applicable skills before editing or executing setup.

**DuckDuckGo:** use `duckduckgo/apple-browsers`. The older `duckduckgo/iOS` repo is archived (1,953 stars at inspection). The [public contributor instructions](https://github.com/duckduckgo/apple-browsers/blob/main/README.md) require initializing submodules, supplying external developer configuration, and removing the private `DuckSansFont` dependency; a system-font fallback is supported. The [upstream UI workflow](https://github.com/duckduckgo/apple-browsers/blob/main/.github/workflows/ios_ui_tests.yml) uses internal runner labels and a private SSH key. The benchmark needs its own public-runner workflow and must disclose the font change when interpreting visual results. Existing project-file and lint instructions in `AGENTS.md` still apply to future edits.

**Proton Pass:** the [README](https://github.com/protonpass/ios-pass/blob/main/README.md) describes its SwiftUI views, UIKit navigation, dependency injection, project and existing tests. The [Rust package downloader](https://github.com/protonpass/ios-pass/blob/main/scripts/public/download_rust_package.sh) downloads a public release asset and verifies the SHA-256 recorded in `.rust-package`; the inspected 2.3.1 asset is publicly available. Review the script before execution: it can install wget and replace local package directories, so do not run it blindly on the user's machine.

The public project nevertheless attaches a missing `scripts/internal/replace_obfuscated_constants.sh` build phase to `iOSUITests`. Its mock test plan also refers to an external mock service. These facts prevent treating its existing UI test scheme as a turnkey public CI setup. A separate app-owned test target and deterministic public fixtures are the proposed path; only a scaffold dry-run has been performed. Normal app buildability has not been disproved by this test-target limitation.

**Excluded initially:** [Proton Mail](https://github.com/ProtonMail/ios-mail/blob/main/README.md) explicitly states that the app cannot currently be built externally because SDK integration uses internal distribution. [Proton VPN](https://github.com/ProtonVPN/ios-mac-app/blob/develop/README.md) requires separate credentials-repository setup and code-signing configuration for VPN entitlements. `brave/brave-ios` is archived. These are weaker first choices for repeatable public Simulator examples.

## Proposed rollout

1. Pin the published UI Action `v0.5.0` or its reviewed commit. Explicit release inputs are available in that version; review and refresh app-owned scaffold files before adopting the new runner/planner behavior.
2. Create independent benchmark forks with upstream attribution. Keep the upstream app revision, harness revision and local integration changes distinguishable.
3. Inspect existing app-owned tests, launch hooks, fixtures and build scripts before scaffolding. Reuse native XCTest and explicit prerequisites; do not assume AXe, Maestro, or another optional inspector is installed.
4. Prove a manual hosted build and a meaningful deterministic UI assertion for each selected app. Preserve build failures and missing prerequisites instead of reporting an empty launch/screenshot check as coverage. Static review scans do not establish a UI pass.
5. Add recurring upstream release comparisons only after the baseline passes. A fork's `release` event does not subscribe to upstream releases: poll upstream metadata or deliberately mirror releases. Pin the resolved app release pair and retain the Action's checkout/head validation. Do not compare a harness-only commit and describe it as the upstream release.
6. Publish per-change coverage, actual screenshots/video/XCTest results and limitations. Do not enable inherited upstream release, deployment, Slack, or issue-management workflows merely to run these checks.

GitHub's [Xcode 27 preview runner inventory](https://github.com/actions/runner-images/blob/main/images/macos/xcode-27-arm64-Readme.md) includes Xcode 27.1 and iOS 27 runtimes as inspected. Verify the supported runner label and installed versions at implementation time; do not assume the ordinary macOS 26 runner contains that Xcode version. Match each pinned app revision to an available toolchain and record the observed preflight.

The machine-readable assessment is stored outside the distributable bundle in the sibling `test-results/popular-ios-apps-2026-11-04/assessment.json` directory. No source code, dependencies, credentials, or app data were downloaded into the toolkit.
