This is a [mkdocs-macros](https://github.com/fralau/mkdocs_macros_plugin/) plugin that shows semver-matching git tag.

The [default `git.tag` variable](https://mkdocs-macros-plugin.readthedocs.io/en/latest/git_info/#catalogue) will match any git tag which might not work with your git workflow ([for example](https://github.com/aquasecurity/tracee/pull/1164#discussion_r757865781)). This plugin adds a new variable `git_semver` that looks only for tags matching the pattern `v*`.

# Usage

## Install

```bash
pip install git+https://github.com/itaysk/mkdocs-macro-gitsemver
# OR
# python3 mkdocs-macro-gitsemver/setup.py install
```

## Import

In `mkdocs.yml`:

```yaml
plugins:
  - macros:
      modules: ["mkdocs_macros_gitsemver"]
```

## Use

In your docs markdown

```
This is version {{ git_semver }}
```
