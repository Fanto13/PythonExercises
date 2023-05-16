const fileList = document.getElementById("file-list");
const folderPath = window.location.pathname.replace("/folders", "");

// Funzione per popolare la lista dei file
function populateFileList() {
  fetch("/read_folder", {
    method: "POST",
    body: JSON.stringify({ folder: folderPath }),
    headers: { "Content-Type": "application/json" },
  })
    .then((response) => response.json())
    .then((data) => {
      fileList.innerHTML = "";

      // Mostra le cartelle
      data.folders.forEach((folder) => {
        const folderName = folder.split("/").pop();
        const folderItem = document.createElement("li");
        const folderLink = document.createElement("a");
        folderLink.href = `/folders/${folder}`;
        folderLink.innerText = folderName;
        folderItem.appendChild(folderLink);
        fileList.appendChild(folderItem);
      });

      // Mostra i file
      data.files.forEach((file) => {
        const fileName = file.split("/").pop();
        const fileItem = document.createElement("li");
        const fileLink = document.createElement("a");
        fileLink.href = `/get_file${folderPath}/${fileName}`;
        fileLink.target = "_blank";
        fileLink.innerText = fileName;

        fileItem.appendChild(fileLink);
        fileList.appendChild(fileItem);
      });
    })
    .catch((error) => console.error(error));
}

// Popola la lista dei file all'avvio della pagina
populateFileList();