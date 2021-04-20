## Jupyter Notebook version control extension

- S3
- GitHub
- Local

```json
{
  "path": "{notebook_name}/{version}/{notebook_name}.ipynb",
  "version": "2021-04-11-14:25:33",
  "message": "version1: init"
}
```

"path": "{notebook_name}/{version}/{notebook_name}.ipynb"

```python
path = "{notebook_name}/{version}/{notebook_name}.ipynb"
version = "2021-04-11-14:25:33"

```

version message信息放在{notebook_name}/version_info.json

```json
{
  "2021-04-11-14:25:33": "version1: init",
  "2021-04-11-14:27:33": "version2: update",
}
```