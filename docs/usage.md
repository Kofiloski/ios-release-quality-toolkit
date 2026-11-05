---
summary: Set up native Simulator checks, select a UI planner, and understand toolkit distribution and privacy boundaries.
read_when:
  - Configuring Xcode access or provider/model/effort after installing the toolkit
  - Understanding execution dependencies, evidence, or delivery channels
---

# Using the toolkit

## Native Simulator setup

Native checks use Xcode tools already exposed to the agent. For external agents, Apple's [MCP setup](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode) requires opening the project in Xcode, allowing external agents in Intelligence settings, and connecting through `xcrun mcpbridge`. The toolkit does not configure an MCP server during installation. If native controls are unavailable, the skills use existing app-local automation and report any verification gap.

When a visible result needs explanation, the skills correlate the reproduction with bounded app logs, relevant saved state, and focused debugger observations using existing Simulator tooling. Raw app state stays local; instrumented observations remain separate from normal test results. See the [Ice Cubes test-app plan](simulator-test-app.md) for a source-backed evaluation flow and its current verification status.

The local verification baseline is Xcode/XCTest and Apple's command-line tools. AXe, third-party MCP servers, and companion CLIs are optional integrations whose availability must be checked; installing the toolkit does not supply or require them.

## Why The Projects Publish Differently

The toolkit presents all three projects as agent skills, but their executable delivery paths are different:

- `app-store-review-risk` and `ios-ui-testability-contract` include Python CLIs, so their release workflows publish attested packages to PyPI in addition to GitHub releases. This gives agents a short `uvx` path for one-off execution and users a clean `pipx` path for persistent installation; GitHub remains canonical for the skills and source.
- `ios-ai-ui-check` is a GitHub Action and reusable workflow. A versioned GitHub release tag is its executable distribution: callers run `Kofiloski/ios-ai-ui-check@v0.6.0` or the matching reusable workflow directly from that ref. Its repository also publishes the installable Agent Skill. The toolkit embeds that guidance, not another copy of the action runtime.

## Choose the UI planner

UI Check `v0.6.0` supports native Anthropic and OpenAI planners, plus an explicitly configured OpenAI-compatible endpoint. Select the provider, model, and effort in the app-owned integration:

```bash
./scripts/local-ai-ui-check.sh --provider anthropic --model claude-sonnet-4-6 --effort high --goal "Verify settings persist"
```

Set `ANTHROPIC_API_KEY` for this example. The matching action inputs are `planner-provider`, `planner-model`, and `planner-effort`. Effort support varies by model; API rejections are preserved without silently changing the requested settings. Existing apps need a scaffold refresh and a `v0.6.0` action pin. These settings configure the optional planner, independently of the coding agent running the skills. Deterministic scenarios and local scanners need no model key. See the [pinned configuration guide](https://github.com/Kofiloski/ios-ai-ui-check/blob/v0.6.0/docs/planner-configuration.md).

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
- "Use Anthropic with claude-sonnet-4-6 at high effort for UI planning."

## Trust boundary

The scanner workflows run locally and do not upload repository contents. Policy reviews retrieve public Apple guidance. Native UI checks use the agent's existing Xcode connection and permissions. The `ios-ai-ui-check` reusable action is provider-agnostic; only an app-owned planner command can choose an external model provider and decide what context it receives. Review all generated changes, workflows, prompts, artifacts, and third-party credentials before use.

The tools provide engineering evidence, not a guarantee of App Store approval, accessibility compliance, or defect-free software.

The toolkit only embeds instructions and references. Follow the canonical project guides to install scanners or refresh an app integration. For local validation and publishing, see [skill maintenance](skill-maintenance.md).
