document.addEventListener("DOMContentLoaded", () => {
  // Модальное окно для входа
  const loginModal = document.getElementById("login-modal");
  const openLoginModal = document.getElementById("open-login-modal");
  const closeLoginModal = document.getElementById("close-login-modal");

  // Проверяем, существуют ли элементы модального окна входа
  if (loginModal && openLoginModal && closeLoginModal) {
    openLoginModal.addEventListener("click", () => {
      loginModal.style.display = "flex";
    });

    closeLoginModal.addEventListener("click", () => {
      loginModal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
      if (event.target === loginModal) {
        loginModal.style.display = "none";
      }
    });
  } else {
    console.warn("Элементы для модального окна входа не найдены в DOM.");
  }

  // Модальное окно для описания
  const infoModal = document.getElementById("info-modal");
  const closeInfoModal = document.getElementById("close-info-modal");

  // Проверяем, существуют ли элементы модального окна описания
  if (infoModal && closeInfoModal) {
    document.querySelectorAll(".log-row").forEach((row) => {
      row.addEventListener("click", () => {
        const description = row.dataset.description || "Описание отсутствует.";
        const response = row.dataset.response || "Меры реагирования отсутствуют.";

        document.getElementById("modal-description").innerText = description;
        document.getElementById("modal-response").innerText = response;

        infoModal.style.display = "flex";
      });
    });

    closeInfoModal.addEventListener("click", () => {
      infoModal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
      if (event.target === infoModal) {
        infoModal.style.display = "none";
      }
    });
  } else {
    console.warn("Элементы для модального окна описания не найдены в DOM.");
  }
});
