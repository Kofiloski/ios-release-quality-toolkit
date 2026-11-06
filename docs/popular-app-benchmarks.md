---
summary: Verified native checks and coverage limits for independent Firefox, DuckDuckGo, and Proton Pass showcase forks.
read_when:
  - Selecting popular open-source iOS apps for public evaluation forks
  - Preparing hosted release-comparison checks for third-party apps
---

# Popular iOS showcase forks

Status: Updated November 6, 2026. All three independent forks now have passing hosted builds and meaningful native UI tests. Downloaded XCTest results verify **three UI tests plus five Proton PRF model tests**, with zero failures or skips. Proton and Firefox also passed locally. DuckDuckGo's local build remains limited by disk space; its hosted keyboard-preference persistence check passed. These are focused native baselines, with no live AI planning or claim of release-wide coverage.

The selected apps are Firefox, DuckDuckGo, and Proton Pass. GitHub metadata inspected on November 4, 2026 reported all three repositories as public, active, and allowing forks. The audience figures below are from that initial inspection. Repository stars measure developer visibility; US App Store rating counts give a separate, imperfect product-audience signal. Neither measure establishes downloads, active users, or the audience a case study would attract.

| App/source | GitHub stars | License reported by source | US App Store ratings displayed |
| --- | --- | --- | --- |
| [Firefox](https://github.com/mozilla-mobile/firefox-ios) | 13,070 | MPL-2.0 | [219K](https://apps.apple.com/us/app/firefox-fast-private-browser/id989804926) |
| [DuckDuckGo](https://github.com/duckduckgo/apple-browsers) | 270 | Apache-2.0, with a separately licensed font excluded | [2.4M](https://apps.apple.com/us/app/duckduckgo-optional-duck-ai/id663592361) |
| [Proton Pass](https://github.com/protonpass/ios-pass) | 302 | GPLv3 or later per README | [8.9K](https://apps.apple.com/us/app/proton-pass-password-manager/id6443490629) |

The initial inspected source trees were Firefox `373f4ae9a082155e5953e8595647316dae2631fd`, DuckDuckGo `838a682e32d0e300c921aae4bf8cf02a203ea5bc`, and Proton Pass `bd22de62d53815d04feeee2da91c9478e71530a0`. These are dated inspection points, not automatically selected release commits. Recheck and pin actual released versions when implementing a comparison.

## Local verification so far

The checkouts are `Firefox-SkillsTest`, `DuckDuckGo-SkillsTest`, and `ProtonPass-SkillsTest` under the owner's iOS projects directory, at the revisions above. Firefox and DuckDuckGo remain branch snapshots. Proton matches tag `1.23.0`; its comparison base is tag `1.22.1` (`6aa48ae7f18cb912ee87bc4f4a5581cc76318c07`). Xcode 27.1 is selected through command-scoped `DEVELOPER_DIR`, with the dedicated iPhone 18 Pro Simulator on iOS 27.0. No external UI inspector or global convenience utility was installed.

- Launch and identifier inventories completed for all three apps. Multiapp source inventories include other products and test fixtures; they do not prove runtime identifiers or routes.
- Firefox's locked JavaScript resources, native app/UI test build and existing `TabsTestsIphone/testAddTabByLongPressTabsButton` passed. One test ran with zero failures/skips, asserting two real tab-tray cells after native tab creation. Reviewed Nimbus code generation and repository-local pinned SwiftLint were exercised. The app/UI-only scheme removes inherited unit `Testables` as well as build entries; selecting `Smoketest` alone did not do this. The fixed native runner rejects unsupported scenario steps and requires one actual passing test. This is branch-snapshot coverage, with no release pair or live AI planning.
- Static App Review scanner runs completed for Firefox and Proton Pass. The whole DuckDuckGo scan exceeded a 120-second local limit; an explicit `--submitted-target DuckDuckGo` replay completed in 55.37 seconds. These are heuristic source reports, without a live policy review or adjudication of findings.
- Proton Pass's existing `PasswordRulesTests` and `PasswordPreferencesTests` passed through the `Entities-Package` scheme: 21 tests, zero failures, with an inspected `.xcresult`. Host `swift test` first failed on an unconditional UIKit import; the library-only `Entities` scheme also lacks a test action. The successful replay used the package's iOS Simulator test scheme.
- DuckDuckGo's documented private-font removal, external-developer configuration and locked dependency resolution are prepared. Its hosted full app/UI build and existing keyboard-preference persistence test passed: one test, no failures/skips. Three native screenshots and the test log verify defaults, both switches changed, navigation, relaunch, and persisted values. The local build stopped at the 1 GiB disk reserve twice, including after Firefox cleanup, with no compiler error; no local DuckDuckGo UI pass is claimed.
- A Proton build-only scheme excludes the upstream actions that modify every booted Simulator or install wget. Its required public Rust package was downloaded with an existing tool and matched the pinned SHA-256. The stock private UI-test target was not run. The public `SkillsPublicUITests` target now runs the real welcome screen, opens the native sign-in form, and verifies the return path without credentials.
- Proton's 24-pin app dependency resolution and complete Simulator test build passed. The first unsigned UI launch failed at the App Group container assertion; ad hoc signing retained those entitlements. A second launch exposed a keychain-group prefix mismatch; matching the Simulator application identifier prefix to the app's checked-in group configuration produced a passing UI replay. App persistence and authentication logic were unchanged. Initial failures, corrected commands, generated entitlements and crash reports were retained.
- The released UI action's planning/execution scripts ran locally in provided-scenario mode without any model key: one UI test passed, with three screenshots, video, `.xcresult`, and explicit release context (309 changed files). The existing PRF input-selection and salt-derivation suites passed five tests. This model coverage and signed-out UI baseline do not verify authenticated release features or a physical passkey ceremony.

The evaluation also produced a narrow identifier-scanner optimization: generated source files without either supported identifier token are skipped before lexing. Replayed Firefox and DuckDuckGo reports were identical to the original reports, while timings fell from 84.39 to 2.40 seconds and 99.70 to 4.29 seconds respectively. The scanner's 45 tests passed, including a large generated-companion regression test. Those findings informed the tooling releases published on November 5, 2026: [UI Check v0.5.0](https://github.com/Kofiloski/ios-ai-ui-check/releases/tag/v0.5.0), [Testability v0.4.3](https://github.com/Kofiloski/ios-ui-testability-contract-skill/releases/tag/v0.4.3), [App Review Risk v0.3.3](https://github.com/Kofiloski/app-store-review-risk/releases/tag/v0.3.3), and [Toolkit v0.2.2](https://github.com/Kofiloski/ios-release-quality-toolkit/releases/tag/v0.2.2). The subsequent planner update shipped [UI Check v0.6.0](https://github.com/Kofiloski/ios-ai-ui-check/releases/tag/v0.6.0) and [Toolkit v0.2.3](https://github.com/Kofiloski/ios-release-quality-toolkit/releases/tag/v0.2.3); these examples use the v0.6.0 runtime.

A later itemized approval removed Proton's completed 2.58 GiB Build folder, recovering 2.44 GiB after backing up and verifying its vendor debug symbols. Logs, `.xcresult`, source and dependency caches were preserved. A separately approved Firefox Build cleanup removed 3.44 GiB of logical products and recovered 2.23 GiB. Its vendor symbols and all local/hosted test evidence were retained. The DuckDuckGo replay still reached the disk reserve, so sequential builds do not imply enough peak headroom.

The first explicitly approved cleanup removed four completed build-product directories (4.33 GiB measured; about 4.51 GiB observed free-space gain), preserving source and test evidence. Further cleanup requires approval of its separately enumerated paths. Run apps sequentially after making sufficient room for dependency extraction and compilation; do not infer space requirements from checkout size.

## Hosted checks

All forks default to `skills-showcase`. Their manual workflows use UI Check v0.6.0 at immutable commit `bde934737ad068298459d9eaecdd8b176b3f8700` with provided scenarios; no model API key is needed. App source and harness revisions are recorded separately. Inherited upstream release, notification and issue workflows are disabled.

| Independent fork | Verified hosted evidence | Scope |
| --- | --- | --- |
| [Proton Pass](https://github.com/Kofiloski/ios-pass/tree/skills-showcase) | [Passed run](https://github.com/Kofiloski/ios-pass/actions/runs/42133167432): 1 UI and 5 PRF model tests; zero failures/skips | Welcome/sign-in round trip and PRF input/salt logic, with 1.22.1 → 1.23.0 release context |
| [Firefox](https://github.com/Kofiloski/firefox-ios/tree/skills-showcase) | [Passed run](https://github.com/Kofiloski/firefox-ios/actions/runs/42133538018): 1 UI test; zero failures/skips | Native tab creation and two actual tab-tray cells; branch snapshot, no release pair |
| [DuckDuckGo](https://github.com/Kofiloski/apple-browsers/tree/skills-showcase) | [Passed run](https://github.com/Kofiloski/apple-browsers/actions/runs/42212517733): 1 UI test; zero failures/skips | Real keyboard switches, navigation and relaunch persistence; branch snapshot and system-font fallback |

Proton's first hosted build passed but comparison setup could not find the pinned base commit in the fork. Its workflow now fetches and validates both exact upstream commits before building; a fresh-checkout preflight and the complete hosted replay passed. DuckDuckGo's first hosted attempt compiled the app but rejected the hard-coded Autofill extension ID under the isolated app ID. The next build passed, but the Network extension embedded by a shell phase bypassed normal build-time validation and failed at Simulator installation. Both Debug Simulator IDs now derive from `APP_ID`, all five embedded extension IDs were verified in Xcode settings, and the helper checks the built app's complete extension list. The complete replay passed one native test in 181.367 seconds. Device identities and production Swift/test logic are unchanged.

The source revisions, integration patches, commands, scan outputs, `.xcresult`, storage audit and current gaps are in the sibling `test-results/popular-ios-local/` directory outside the distributable bundle. All three have hosted UI proof; Proton and Firefox also have local UI evidence. DuckDuckGo local UI validation remains limited by disk space. No live Anthropic or other model planning was exercised in these keyless examples.

## Build and test feasibility

**Firefox:** the current [root README](https://github.com/mozilla-mobile/firefox-ios/blob/main/README.md) specifies Xcode 27.1. The [app README](https://github.com/mozilla-mobile/firefox-ios/blob/main/firefox-ios/README.md) describes Node/bootstrap preparation and the `Fennec` scheme. Existing unit and UI tests should be reused after inspecting the exact release's launch hooks. The checked-in GitHub UI workflow still references older Xcode/runner combinations and includes Slack reporting; do not copy or enable it wholesale in a benchmark fork. Read its `AGENTS.md`, contribution guide, bootstrap script, and applicable skills before editing or executing setup.

**DuckDuckGo:** use `duckduckgo/apple-browsers`. The older `duckduckgo/iOS` repo is archived (1,953 stars at inspection). The [public contributor instructions](https://github.com/duckduckgo/apple-browsers/blob/main/README.md) require initializing submodules, supplying external developer configuration, and removing the private `DuckSansFont` dependency; a system-font fallback is supported. The [upstream UI workflow](https://github.com/duckduckgo/apple-browsers/blob/main/.github/workflows/ios_ui_tests.yml) uses internal runner labels and a private SSH key. The benchmark needs its own public-runner workflow and must disclose the font change when interpreting visual results. Existing project-file and lint instructions in `AGENTS.md` still apply to future edits.

**Proton Pass:** the [README](https://github.com/protonpass/ios-pass/blob/main/README.md) describes its SwiftUI views, UIKit navigation, dependency injection, project and existing tests. The [Rust package downloader](https://github.com/protonpass/ios-pass/blob/main/scripts/public/download_rust_package.sh) downloads a public release asset and verifies the SHA-256 recorded in `.rust-package`; the inspected 2.3.1 asset is publicly available. Review the script before execution: it can install wget and replace local package directories, so do not run it blindly on the user's machine.

The public project nevertheless attaches a missing `scripts/internal/replace_obfuscated_constants.sh` build phase to `iOSUITests`. Its mock test plan also refers to an external mock service. These facts prevent treating its existing UI test scheme as a turnkey public CI setup. The independent fork now uses a separate app-owned public target and the app's existing UI-test launch hook. A local native UI replay passed without replacing app logic. Its public helper uses macOS `curl` with the upstream Rust version/checksum and skips automatic source formatting during checks.

**Excluded initially:** [Proton Mail](https://github.com/ProtonMail/ios-mail/blob/main/README.md) explicitly states that the app cannot currently be built externally because SDK integration uses internal distribution. [Proton VPN](https://github.com/ProtonVPN/ios-mac-app/blob/develop/README.md) requires separate credentials-repository setup and code-signing configuration for VPN entitlements. `brave/brave-ios` is archived. These are weaker first choices for repeatable public Simulator examples.

## Maintaining the examples

1. Pin UI Action `v0.6.0` or its reviewed commit. Explicit release inputs and provider/model/effort selection are available in that version; review and refresh app-owned scaffold files before adopting the new runner/planner behavior.
2. Maintain the independent benchmark forks with upstream attribution. Keep the upstream app revision, harness revision and local integration changes distinguishable.
3. Inspect existing app-owned tests, launch hooks, fixtures and build scripts before scaffolding. Reuse native XCTest and explicit prerequisites; do not assume AXe, Maestro, or another optional inspector is installed.
4. On each source refresh, prove a manual hosted build and a meaningful deterministic UI assertion for each selected app. Preserve build failures and missing prerequisites instead of reporting an empty launch/screenshot check as coverage. Static review scans do not establish a UI pass.
5. Add recurring upstream release comparisons only after the baseline passes. A fork's `release` event does not subscribe to upstream releases: poll upstream metadata or deliberately mirror releases. Pin the resolved app release pair and retain the Action's checkout/head validation. Do not compare a harness-only commit and describe it as the upstream release.
6. For case studies, publish per-change coverage, actual screenshots/video/XCTest results and limitations. Workflow parent artifacts are retained for 14 days, so download evidence for longer-lived materials. Do not enable inherited upstream release, deployment, Slack, or issue-management workflows merely to run these checks.

GitHub's [Xcode 27 runner inventory](https://github.com/actions/runner-images/blob/main/images/macos/xcode-27-arm64-Readme.md) includes Xcode 27.1 and iOS 27 runtimes as inspected on November 5. The Proton example selects `xcode-27` and Xcode 27.1 explicitly. Verify the supported runner label and installed versions at implementation time; do not assume the ordinary macOS 26 runner contains that Xcode version. Match each pinned app revision to an available toolchain and record the observed preflight.

The machine-readable assessment is stored outside the distributable bundle in the sibling `test-results/popular-ios-apps-2026-11-04/assessment.json` directory. No source code, dependencies, credentials, or app data were downloaded into the toolkit.

## Release-diff generation

The three forks now have a separate `skills-release-regression.yml` workflow,
pinned to the reviewed, unreleased action implementation
`fec98e75076c9f07aa9c47b017b6998d64b98d19`. It discovers stable iOS tags, compares
immutable previous/new commits, applies only the app-owned harness, and generates
new JSON scenarios for native XCTest. Cases cite changed files; uncovered changes
remain explicit. The fixed baseline passes above remain separate evidence.

The implementation separates uncredentialed app builds/tests from credentialed
planning and write-enabled publication. Reports and evidence are retained as
immutable attempt assets on each fork's `ui-check-*` releases. `ui-check-state`
persists a queue, including later hotfixes. First discovery starts at the latest
pair; manual inputs replay older pairs. Daily polling was enabled on all three
forks on November 7, 2026 (Europe/Skopje), at the owner's explicit request:
`ENABLE_RELEASE_CHECKS=true`, with each workflow active on `skills-showcase`.
The schedule polls at 07:17 UTC daily. No planner key is configured, so new
comparisons produce blocked reports and skip macOS work until credentials are
supplied. Enabling the schedule does not establish live generated UI coverage.

| Fork | Credential-gate verification | Selected pair |
| --- | --- | --- |
| [Kofiloski/ios-pass](https://github.com/Kofiloski/ios-pass) | [Blocked as expected; report archived](https://github.com/Kofiloski/ios-pass/actions/runs/42296867037) | 1.22.1 → 1.23.0 |
| [Kofiloski/firefox-ios](https://github.com/Kofiloski/firefox-ios) | [Blocked as expected; report archived](https://github.com/Kofiloski/firefox-ios/actions/runs/42296868891) | firefox-v159.1 → firefox-v160.0 |
| [Kofiloski/apple-browsers](https://github.com/Kofiloski/apple-browsers) | [Blocked as expected; report archived](https://github.com/Kofiloski/apple-browsers/actions/runs/42296870893) | 7.243.0+ios → 7.244.0+ios |

These hosted runs skipped macOS and generation because no model key is configured.
They verified discovery, missing-key gating and durable report publication,
not generated test quality or a new release's native UI pass. The action's 132
maintenance tests passed locally, including generic Swift SDK typechecking;
fixture provider transport is separate from live Anthropic/OpenAI access. See the
[action release-flow documentation](https://github.com/Kofiloski/ios-ai-ui-check/blob/main/docs/release-regressions.md)
and each fork's setup instructions before enabling scheduling.

Release harness preflight passed for Proton and Firefox. DuckDuckGo's stable
release reorders PBX objects, so a snapshot-context patch failed before any build.
Its release profile now prepares that file with an app-owned helper, preserving
all parsed settings except private-font removal and two Debug Simulator overrides.
That helper passed against both source snapshots, and the remaining overlay
applies cleanly. This source preparation is separate from a full release build or
live model-generated UI execution.
