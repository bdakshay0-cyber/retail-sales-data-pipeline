CREATE TABLE PipelineAudit
(
    AuditID INT IDENTITY(1,1) PRIMARY KEY,
    PipelineName VARCHAR(200),
    PipelineRunID VARCHAR(200),
    Status VARCHAR(50),
    RowsProcessed INT,
    StartTime DATETIME2,
    EndTime DATETIME2,
    ErrorMessage VARCHAR(MAX),
    CreatedDate DATETIME2 DEFAULT GETDATE()
);
