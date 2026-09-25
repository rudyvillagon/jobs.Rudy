const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
}
const gradeAvg = student.grades.map(g => g.grade).reduce((acc, val) => acc + val, 0)/ student.grades.length; 

const highestGrade = student.grades.reduce((max, current) => current.grade > max.grade ? current : max );

const lowestGrade = student.grades.reduce((min, current) => current.grade < min.grade ? current : min );


const result = {
	name : student.name,
	gradeAvg : gradeAvg,
	highestGrade : highestGrade.name,
	lowestGrade : lowestGrade.name,
}

console.log(result)