<!-- API / service / framework template. Pattern: fastapi/express/stripe-node
     (see project-types.md). Hello-world EARLY, often before install (express
     6-line app). Prominent docs-site pointer. Version-support policy.
     Best-in-class: graduated tutorial (fastapi create→run→check). -->

# {name}

![CI](https://github.com/{owner}/{repo}/actions/workflows/{ci}.yml/badge.svg?branch=main)
![coverage]({coverage-badge})
![{registry} version](https://img.shields.io/npm/v/{pkg})

{One sentence: what it does and for whom. ≤120 chars.}

**Documentation:** {docs-site} · **Source:** https://github.com/{owner}/{repo}

<!-- Hello-world BEFORE install — prove the surface is small. -->
```{lang}
{minimal complete server/client — the express 6-line ideal}
```

## Requirements

{Runtime + minimum version, stated as policy: "Node.js 20+ (even-numbered LTS releases)."}

## Install

```sh
{registry one-liner}
```

## Quick start

<!-- Graduated tutorial (fastapi pattern): create → run (with expected terminal
     output) → verify. Each step's output shown. -->
1. Create `{file}`:
   ```{lang}
   {code}
   ```
2. Run it:
   ```sh
   $ {run command}
   {expected output}
   ```
3. {Verify step — curl the endpoint and show the response.}

## Configuration

{The 2–3 options everyone needs, then:} Full reference: {docs link}.

## Performance

<!-- Only with reproducible numbers and disclosed methodology; otherwise delete. -->

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[{SPDX id}](LICENSE) © {owner}
