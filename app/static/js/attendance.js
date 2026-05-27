async function markAttendance(studentId) {

    const response = await fetch('/mark', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            student_id: studentId,
            status: 'Present'
        })
    });

    const data = await response.json();

    alert(data.message);
}