# data-pipeline

Utilities for parsing Pentaho transformation XML and uploading lineage
information to Open Metadata.

## Uploading Pentaho Lineage

1. Install requirements:

```bash
pip install -r requirements.txt
```

2. Run the upload script:

```bash
python scripts/upload_lineage.py path/to/transformation.xml --api http://<openmetadata-host>:8585/api --token <OM_TOKEN>
```

You can also set the ``OM_TOKEN`` environment variable instead of using
``--token``.

