CREATE PROCEDURE InsertPipelineAudit
    @PipelineName VARCHAR(200),
    @PipelineRunID VARCHAR(200),
    @Status VARCHAR(50),
    @RowsProcessed INT,
    @StartTime DATETIME2,
    @EndTime DATETIME2,
    @ErrorMessage VARCHAR(MAX) = NULL
AS
BEGIN

    INSERT INTO PipelineAudit
    (
        PipelineName,
        PipelineRunID,
        Status,
        RowsProcessed,
        StartTime,
        EndTime,
        ErrorMessage
    )
    VALUES
    (
        @PipelineName,
        @PipelineRunID,
        @Status,
        @RowsProcessed,
        @StartTime,
        @EndTime,
        @ErrorMessage
    );

END;
