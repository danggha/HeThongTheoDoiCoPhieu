/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [symbol]
      ,[price]
      ,[change]
      ,[last_refreshed]
  FROM [CoPhieu].[dbo].[StockInfo]