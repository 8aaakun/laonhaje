document.addEventListener("DOMContentLoaded", function () {
    const eventInput = document.getElementById("eventInput");
    const eventDate = document.getElementById("eventDate");
    const addEventButton = document.getElementById("addEventButton");
    const calendarDiv = document.getElementById("calendarDays");
    const eventListDiv = document.getElementById("eventList");
    const yearSelect = document.getElementById("yearSelect");
    const monthSelect = document.getElementById("monthSelect");

    const events = [];
    let currentYear, currentMonth;

    function generateCalendar(year, month) {
        const daysInMonth = new Date(year, month + 1, 0).getDate();
        const firstDayOfWeek = new Date(year, month, 1).getDay();

        calendarDiv.innerHTML = "";

        const header = document.createElement("div");
        header.classList.add("calendar-header");
        header.innerHTML = `${year}년 ${month + 1}월`;
        calendarDiv.appendChild(header);

        const daysContainer = document.createElement("div");
        daysContainer.classList.add("calendar-days");

        const weekdays = ["일", "월", "화", "수", "목", "금", "토"];
        for (const weekday of weekdays) {
            const weekdayDiv = document.createElement("div");
            weekdayDiv.classList.add("calendar-day", "weekday");
            weekdayDiv.textContent = weekday;
            daysContainer.appendChild(weekdayDiv);
        }

        for (let i = 0; i < firstDayOfWeek; i++) {
            const emptyDay = document.createElement("div");
            emptyDay.classList.add("calendar-day", "empty-day");
            daysContainer.appendChild(emptyDay);
        }

        for (let day = 1; day <= daysInMonth; day++) {
            const dayDiv = document.createElement("div");
            dayDiv.classList.add("calendar-day");
            dayDiv.textContent = day;

            daysContainer.appendChild(dayDiv);
        }

        calendarDiv.appendChild(daysContainer);
    }

    function updateCalendar() {
        generateCalendar(currentYear, currentMonth);
    }

    function updateEventList() {
        eventListDiv.innerHTML = "";
        for (const event of events) {
            const eventDiv = document.createElement("div");
            eventDiv.classList.add("event");
            eventDiv.innerText = event.title + " - " + event.date;
            eventDiv.addEventListener("click", function () {
                deleteEvent(event);
            });
            eventListDiv.appendChild(eventDiv);
        }
    }

    function deleteEvent(event) {
        const index = events.indexOf(event);
        if (index !== -1) {
            events.splice(index, 1);
            updateEventList();
        }
    }

    addEventButton.addEventListener("click", function () {
        const newEvent = {
            title: eventInput.value.trim(),
            date: eventDate.value,
        };

        if (newEvent.title !== "") {
            events.push(newEvent);
            eventInput.value = "";
            eventDate.value = "";
            updateEventList();
        }
    });

    const currentDate = new Date();
    currentYear = currentDate.getFullYear();
    currentMonth = currentDate.getMonth();
    generateCalendar(currentYear, currentMonth);
    updateEventList();

    yearSelect.addEventListener("change", function () {
        currentYear = parseInt(this.value);
        updateCalendar();
    });

    monthSelect.addEventListener("change", function () {
        currentMonth = parseInt(this.value);
        updateCalendar();
    });

    document
        .getElementById("prevMonth")
        .addEventListener("click", function () {
            currentMonth--;
            if (currentMonth < 0) {
                currentMonth = 11;
                currentYear--;
            }
            updateYearSelect();
            updateMonthSelect();
            updateCalendar();
        });

    document
        .getElementById("nextMonth")
        .addEventListener("click", function () {
            currentMonth++;
            if (currentMonth > 11) {
                currentMonth = 0;
                currentYear++;
            }
            updateYearSelect();
            updateMonthSelect();
            updateCalendar();
        });

    function updateYearSelect() {
        const currentYear = new Date().getFullYear();

        for (let year = currentYear - 10; year <= currentYear + 10; year++) {
            const option = document.createElement("option");
            option.value = year;
            option.textContent = year;
            yearSelect.appendChild(option);
        }

        yearSelect.value = currentYear;
    }

    function updateMonthSelect() {
        for (let month = 0; month < 12; month++) {
            const option = document.createElement("option");
            option.value = month;
            option.textContent = month + 1 + "월";
            monthSelect.appendChild(option);
        }

        monthSelect.value = currentMonth;
    }

    updateYearSelect();
    updateMonthSelect();
});