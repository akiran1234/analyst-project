connect system/admin                                         # connect to system admin 
drop user scott cascade;                                      # dropping scott user if exists user/schema both same in oracle.
create user scott identified by tiger;                 
grant all privileges to scott;
connect scott
@C:\Users\Kiran\Downloads\oracle\SCOTT.sql