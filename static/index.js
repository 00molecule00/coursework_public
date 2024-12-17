function deleteNote(noteId) {
    fetch(`/delete-note/${noteId}`, {
        method: 'GET',
    }).then((_res) => {
        window.location.href = "/home";
    });
}

  
  function editNote(noteId, newNote) {
    fetch(`/edit-note/${noteId}`, {
      method: "POST",
      body: JSON.stringify({ newNote: newNote }),
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((res) => res.json())
      .then((data) => {
        if (data.status === 'success') {
          window.location.href = "/";
        } else {
          console.error(data.message);
        }
      });
  }
  
  function addNote() {
    const noteText = document.getElementById('note').value;

    fetch('/add-note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ newNote: noteText }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Optionally, you can handle the response here, e.g., show a message to the user.
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle errors if necessary.
    });
}
