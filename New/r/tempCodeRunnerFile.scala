import org.apache.spark.sql.functions.rand

// Generate random DataFrame with employee data
val employeeData = Seq(
  ("Aarav", "Patel", 1001, "Engineering"),
  ("Aisha", "Sharma", 1002, "HR"),
  ("Advik", "Singh", 1003, "Engineering"),
  ("Ananya", "Joshi", 1004, "Sales"),
  ("Arjun", "Kumar", 1005, "HR")
)
val employeeDF = spark.createDataFrame(employeeData).toDF("first_name", "last_name", "employee_id", "department_id")

// Generate random DataFrame with department data
val departmentData = Seq(
  (1001, "Engineering"),
  (1002, "HR"),
  (1003, "Engineering"),
  (1004, "Sales"),
  (1005, "HR")
)
val departmentDF = spark.createDataFrame(departmentData).toDF("department_id", "department_name")

// Generate Bloom filters for department IDs of both datasets
import org.apache.spark.util.sketch.BloomFilter
val bloomFilterEmployee = employeeDF.select("department_id").stat.bloomFilter("department_id", 5, 0.1)
val bloomFilterDepartment = departmentDF.select("department_id").stat.bloomFilter("department_id", 5, 0.1)

// Broadcast Bloom filters to all worker nodes
val broadcastBloomFilterEmployee = spark.sparkContext.broadcast(bloomFilterEmployee)
val broadcastBloomFilterDepartment = spark.sparkContext.broadcast(bloomFilterDepartment)

// Perform Bloom join to find employees belonging to the same department
val joinedDF = employeeDF.filter(row => broadcastBloomFilterDepartment.value.mightContain(row.getInt(2)))
  .join(departmentDF.filter(row => broadcastBloomFilterEmployee.value.mightContain(row.getInt(0))), "department_id")

// Show or further process the joined DataFrame
joinedDF.show()
