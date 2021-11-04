const api_key = "79b1598a381148b48f6800688c9d4a86";
const base_url = "https://api.rawg.io/api/games";

const App = {
  delimiters: ["[[", "]]"],
  data() {
    return {
      gamesSevenAgoList: [],
      gamesSevenAheadList: [],
      wishlistGames: [],
      searchTerm: "",
      searchResults: [],
      searchDate: "",
      todayDate:"",
    };
  },

  methods: {
    gamesSevenAgo() {
      this.dateCalcMinus7()
      axios({
        method: "get",
        url: base_url,
        headers: {
          "Content-Type": "application/json",
        },
        params: {
          key: api_key,
          dates: this.searchDate + "," + this.todayDate,
          page_size: 12,
          ordering: "released",
        },
      }).then((response) => {
        this.gamesSevenAgoList = response.data.results;
      });
    },
    gamesSevenAhead() {
      this.dateCalcPlus7()
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
          dates: this.todayDate + "," + this.searchDate,
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
        console.log(response.data);
        this.searchResults = response.data.results;
        this.searchTerm = "";
      });
    },
    addToList(game){
      console.log(game)
    },
    todayDateCalc() {
      var date = new Date();
      var dd = String(date.getDate()).padStart(2, "0");
      var mm = String(date.getMonth() + 1).padStart(2, "0");
      var yyyy = String(date.getFullYear());
      date = yyyy + '-' + mm + '-' + dd;
      this.todayDate = date;
    },
    dateCalcPlus7() {
      var date = new Date();
      date.setDate(date.getDate() + 7);
      var dd = String(date.getDate()).padStart(2, "0");
      var mm = String(date.getMonth() + 1).padStart(2, "0");
      var yyyy = String(date.getFullYear());
      date = yyyy + '-' + mm + '-' + dd;
      this.searchDate = date;
    },
    dateCalcMinus7() {
      var date = new Date();
      date.setDate(date.getDate() - 7);
      var dd = String(date.getDate()).padStart(2, "0");
      var mm = String(date.getMonth() + 1).padStart(2, "0");
      var yyyy = String(date.getFullYear());
      date = yyyy + '-' + mm + '-' + dd;
      this.searchDate = date;
    },
  },

  created() {
    this.todayDateCalc();
    this.gamesSevenAgo();
    this.gamesSevenAhead();
  },
};
Vue.createApp(App).mount("#app");
