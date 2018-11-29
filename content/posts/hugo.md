+++
draft = false
date = "2018-06-04"
title = "Hugo"
slug = "hugo"
tags = ["cheatsheet", "golang", "web", "tools"]
categories = ["tools", "web", "cheatsheet", "golang"]
+++

`hugo` is a static website generator developed in golang.

##### Create a New Site

```
hugo new site [SITE_NAME]
```

##### Add a theme

```
cd [SITE_NAME]
git init
git submodule add [THEME_REPO_URL]

echo 'theme = "[THEME_NAME]"' >> config.toml
```