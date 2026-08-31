# Azure Data Factory ARM Templates

This folder contains deployment artifacts exported from Azure Data Factory.

## Contents

### ARMTemplateForFactory.json
Main ARM deployment template.

### ARMTemplateParametersForFactory.json
Parameters used when deploying the ADF template.

### factory/
Contains factory-specific exported ARM templates.

### linkedTemplates/
Contains linked ARM templates generated when the complete deployment template is split into multiple files.

These templates support infrastructure deployment and reproducibility of the Azure Data Factory environment.
