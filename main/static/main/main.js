const api_key = "79b1598a381148b48f6800688c9d4a86";
const base_url = "https://api.rawg.io/api/games";

const App = {
  delimiters: ["[[", "]]"],
  data() {
    return {
      gamesSevenAgoList: [],
      gamesSevenAheadList: [],
      gamesTodayList: [],
      wishlistGames: [],
      listIds: [],
      searchTerm: "",
      searchResults: [],
      todayDate: "",
      startDate: "",
      endDate: "",
      startDateA: "",
      endDateA: "",
      csrfmiddlewaretoken: "",
    };
  },
  methods: {
    getWishedId() {
      axios({
        method: "get",
        url: "/getWishedId/",
      }).then((response) => {
        this.listIds = response.data.api_id;
        this.getWishlistGames();
      });
    },
    removeFromList(game) {
      axios({
        method: "post",
        url: "/removeGame/",
        data: {
          game,
        },
        headers: {
          "X-CSRFToken": this.csrfmiddlewaretoken,
        },
      })
        .then(() => this.getWishedId())
        .then(() => this.getWishlistGames());
    },
    addToList(game) {
      axios({
        method: "post",
        url: "/addToList/",
        data: {
          game,
        },
        headers: {
          "X-CSRFToken": this.csrfmiddlewaretoken,
        },
      })
        .then(() => this.getWishedId())
        .then(() => this.getWishlistGames());
    },
    getWishlistGames() {
      this.wishlistGames = [];
      for (let i = 0; i < this.listIds.length; i++) {
        axios({
          method: "get",
          url: base_url + "/" + this.listIds[i],
          headers: {
            "Content-Type": "application/json",
          },
          params: {
            key: api_key,
          },
        }).then((response) => {
          this.wishlistGames.push(response.data);
        });
      }
    },
    gamesToday() {
      this.todayDateCalc();
      axios({
        method: "get",
        url: base_url,
        headers: {
          "Content-Type": "application/json",
        },
        params: {
          key: api_key,
          dates: this.todayDate + "," + this.todayDate,
          page_size: 12,
          ordering: "released",
        },
      }).then((response) => {
        this.gamesTodayList = response.data.results;
      });
    },
    gamesSevenAgo() {
      this.dateCalcMinus7();
      axios({
        method: "get",
        url: base_url,
        headers: {
          "Content-Type": "application/json",
        },
        params: {
          key: api_key,
          dates: this.startDateA + "," + this.endDateA,
          page_size: 12,
          ordering: "released",
        },
      }).then((response) => {
        this.gamesSevenAgoList = response.data.results;
      });
    },
    gamesSevenAhead() {
      this.dateCalcPlus7();
      axios({
        method: "get",
        url: base_url,
        headers: {
          "Content-Type": "application/json",
        },
        params: {
          key: api_key,
          page_size: 12,
          ordering: "released",
          dates: this.startDate + "," + this.endDate,
        },
      }).then((response) => {
        this.gamesSevenAheadList = response.data.results;
      });
    },
    searchGame() {
      console.log(this.searchTerm);
      axios({
        method: "get",
        url: base_url,
        headers: {
          "Content-Type": "application/json",
        },
        params: {
          key: api_key,
          search_precise: true,
          page_size: 12,
          search: this.searchTerm,
        },
      }).then((response) => {
        this.searchResults = response.data.results;
        this.searchTerm = "";
      });
    },
    todayDateCalc() {
      var date = new Date();
      var dd = String(date.getDate()).padStart(2, "0");
      var mm = String(date.getMonth() + 1).padStart(2, "0");
      var yyyy = String(date.getFullYear());
      date = yyyy + "-" + mm + "-" + dd;
      this.todayDate = date;
    },
    dateCalcPlus7() {
      var startDate = new Date();
      startDate.setDate(startDate.getDate() + 1);
      var dd = String(startDate.getDate()).padStart(2, "0");
      var mm = String(startDate.getMonth() + 1).padStart(2, "0");
      var yyyy = String(startDate.getFullYear());
      startDate = yyyy + "-" + mm + "-" + dd;
      this.startDate = startDate;
      var date = new Date();
      date.setDate(date.getDate() + 7);
      var dd = String(date.getDate()).padStart(2, "0");
      var mm = String(date.getMonth() + 1).padStart(2, "0");
      var yyyy = String(date.getFullYear());
      date = yyyy + "-" + mm + "-" + dd;
      this.endDate = date;
    },
    dateCalcMinus7() {
      var startDate = new Date();
      startDate.setDate(startDate.getDate() - 7);
      var dd = String(startDate.getDate()).padStart(2, "0");
      var mm = String(startDate.getMonth() + 1).padStart(2, "0");
      var yyyy = String(startDate.getFullYear());
      startDate = yyyy + "-" + mm + "-" + dd;
      this.startDateA = startDate;
      var date = new Date();
      date.setDate(date.getDate() - 1);
      var dd = String(date.getDate()).padStart(2, "0");
      var mm = String(date.getMonth() + 1).padStart(2, "0");
      var yyyy = String(date.getFullYear());
      date = yyyy + "-" + mm + "-" + dd;
      this.endDateA = date;
    },
  },
  mounted() {
    this.csrfmiddlewaretoken = document.querySelector(
      'input[name="csrfmiddlewaretoken"]'
    ).value;
  },
  created() {
    this.gamesToday();
    this.gamesSevenAgo();
    this.gamesSevenAhead();
    this.getWishedId();
  },
};
Vue.createApp(App).mount("#app");
