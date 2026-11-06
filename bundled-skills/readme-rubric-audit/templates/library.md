<!-- Library/package template. Pattern: requests/zod/axios (see project-types.md).
     Decide first: gateway README (docs site exists → stay slim) or reference
     README (README is the docs). This skeleton is the gateway; grow API
     sections only deliberately. -->

# {project-name}

![{registry} version](https://img.shields.io/npm/v/{pkg})
![CI](https://github.com/{owner}/{repo}/actions/workflows/{ci}.yml/badge.svg?branch=main)
![downloads](https://img.shields.io/npm/dm/{pkg})

{One sentence: what it does and for whom. ≤120 chars. Must match the repo description.}

<!-- Teaser BEFORE install — show the API's feel in ≤10 lines (requests/zod pattern). -->
```{lang}
{minimal-but-real snippet showing the core API}
```

## Highlights

- {capability, stated as fact, not adjective}
- {what differentiates it from the named alternatives}
- {constraint honesty: zero-dependency / typed / etc. — only if true}

## Install

```sh
{registry one-liner, e.g. npm install pkg}
```

<!-- Prerequisites only if non-obvious: "Requires Node 20+." One line. -->

## Usage

<!-- Minimal working example WITH expected output. Ship it as a runnable file
     in the repo where practical. -->
```{lang}
{example}
```
```
{expected output}
```

{Second example only if it teaches a genuinely different concept; otherwise link out.}

## API

See {docs-site-or-API.md link}. <!-- Gateway: one line. Reference README: grow tables here deliberately. -->

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). {One line on where questions go: issues/discussions/chat.}

## License

[{SPDX id}](LICENSE) © {owner}
