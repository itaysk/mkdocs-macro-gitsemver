This is a [mkdocs-macros](https://github.com/fralau/mkdocs_macros_plugin/) plugin that shows the git tag of the latest version.  
The [default `git.tag` variable](https://mkdocs-macros-plugin.readthedocs.io/en/latest/git_info/#catalogue) will match any git tag which might not work with your git workflow ([for example](https://github.com/aquasecurity/tracee/pull/1164#discussion_r757865781)). This plugin adds a new variable `git_tag_version` that looks only for tags matching the pattern `v*`.

# Usage

## Install

```bash
pip install git+https://github.com/itaysk/mkdocs-macros-gittagversion
# OR
# python3 mkdocs-macros-gittagversion/setup.py install
```

## Import

In `mkdocs.yml`:

```yaml
plugins:
  - macros:
      modules: ["mkdocs_macros_gittagversion"]
```

## Use

In your docs markdown

```
This is version {{ git_tag_version }}
```
