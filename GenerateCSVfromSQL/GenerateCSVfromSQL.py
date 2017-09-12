import DBAccessor as dbac

rows = dbac.DBAccessor.ExecuteQuery("SELECT * FROM CORRECTED_GPS_modified")
print(rows)