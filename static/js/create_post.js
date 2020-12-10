function submitForm(ev) {
    const formData = new FormData(this);

    const data = {
        title: formData.get('title'),
        text: formData.get('text'),
        blog_id: formData.get('blog_id'),
    };

    const headers = {
        'content-type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken'),
    };

    fetch('/api/blogs/', {
        method: 'post',
        headers: headers,
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(json => console.log(json))
        .catch(err => console.log(err));

    ev.preventDefault();
    return false;
}

document.querySelector('#form-create-post')
    .addEventListener('submit', submitForm);
