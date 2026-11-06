<!-- Research / data project template. Pattern: whisper/segment-anything/
     alphafold (see project-types.md). NO badges — bracket-link nav instead
     (observed in all sampled research repos). Citation block required.
     License per artifact when code/weights/data differ (alphafold pattern). -->

# {project-name}

[[`Paper`]({arxiv-url})] [[`Project page`]({page-url})] [[`Demo/Colab`]({colab-url})] [[`BibTeX`](#citation)]

{One sentence: what the method/dataset is and what problem it addresses.}

<!-- Architecture diagram or key-results figure. Alt text always; never encode
     critical info only in the image. -->
![{approach diagram}]({diagram.png})

{2–3 sentences of approach summary, written for a reader deciding whether the
paper is relevant — not the abstract pasted verbatim.}

## Setup

```sh
{environment creation + install, pinned for reproduction}
```

{Hardware requirements stated plainly: GPU/VRAM/disk.}

## Models / data

<!-- Download table with sizes — whisper pattern. Only artifacts that exist. -->
| Name | Params | Size | Download |
|---|---|---|---|
| {model} | {n} | {size} | [link]({url}) |

## Usage

```sh
{CLI invocation}
```

```{lang}
{library usage — both where both exist (whisper pattern)}
```

## Results

<!-- Headline numbers + exact reproduction command. If results can't be
     reproduced from this repo, say what's missing (alphafold's CASP14
     caveat is the honesty model). -->

## Citation

```bibtex
{bibtex entry}
```

## License

{Code: SPDX + link. If weights/data carry different terms, one line each —
never let a reader assume the code license covers the weights.}
