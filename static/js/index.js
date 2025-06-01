const likedPosts = JSON.parse(document.getElementById("liked-posts").textContent);
const likes = document.querySelectorAll(".like");
likes.forEach(e => {
    e.addEventListener('submit', (event) => {
        event.preventDefault();
        const formData = new FormData(e);
        fetch(e.action, {
            method: "POST",
            body: formData
        })
        .then(resp => resp.text())
        .then(resp => {
            console.log(e)
            const like = e.querySelector("span");
            const heart = e.querySelector(".heart")
            if(!likedPosts[e.getAttribute("data-id")]){
                like.innerText = `${parseInt(like.innerText)+1}`;
                heart.classList.add('active');
                heart.classList.add('anim');
            } else {
                like.innerText = `${parseInt(like.innerText)-1}`;
                heart.classList.remove('active');
                heart.classList.remove('anim');
            }
            likedPosts[e.getAttribute("data-id")] = !likedPosts[e.getAttribute("data-id")];
        })
    })
})
