[mkdocs-macros](https://github.com/fralau/mkdocs_macros_plugin/) plugin that shows semver-matching git tag.

The [default `git.tag` variable](https://mkdocs-macros-plugin.readthedocs.io/en/latest/git_info/#catalogue) will match any git tag, this adds a new variable `gitsemver` that looks only for tags matching the pattern `v*`.
