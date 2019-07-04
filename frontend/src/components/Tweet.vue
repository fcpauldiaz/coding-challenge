<template>
  <div>
    <div class="margin-bottom">
      <!-- add model and max length validation-->
      <input type="text" placeholder="What's your name?" v-model="new_tweet_author" v-bind:maxlength="50">
      <input type="text" placeholder="What's on your mind?" v-model="new_tweet_content" v-bind:maxlength="50">
      <button v-on:click="addTweet">Post Tweet</button>
    </div>
    <div class="center">
      <div class="margin-bottom">
        <span><input type="checkbox" v-model="sort_by_date">Sort By Date</span>
        <span><input type="checkbox" v-model="sort_by_name">Sort by Name</span>
      </div>
      <table class="margin">
        <thead>
            <tr>
              <th>Date</th>
              <th>Name</th>
              <th>Content</th>
            </tr>
        </thead>
        <tbody>
            <!-- show all tweets in current model-->
            <!-- For production I would actually make a Tweet Component to render each one -->
            <tr v-for="tweet in tweets" v-bind:key="tweet.id">
                <td>{{ formatDate(tweet.created_at) }}</td>
                <td>{{ tweet.name }}</td>
                <td>{{ tweet.content }}</td>
            </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Tweet',
  data() {
    return {
      new_tweet_content: '',
      new_tweet_author: '',
      tweets: [],
      sort_by_name: false,
      sort_by_date: false,
    }
  },
  props: {
    msg: String
  },
  mounted() {
    // fetch all tweets at start/mounted component
    fetch("http://127.0.0.1:8000/tweet/")
    .then(resp => resp.json()) // Transform the data into json
    .then(data => this.tweets = data);
  },
  methods: {
    addTweet: function() {
      // validate tweet
      if (this.new_tweet_content === '' || this.new_tweet_author === '') {
        alert('Your tweet should have an author and/or content please!');
        return;
      }
      const promise = fetch('http://127.0.0.1:8000/tweet/', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          name: this.new_tweet_author,
          content: this.new_tweet_content,
        })
      });
      promise
        .then(r => r.json())
        .then((tweet) => {
          // add async tweet to table.
          this.tweets.push(tweet);
        });
    },
    sort: function() {
      // check type of sort
      if (this.sort_by_name.active === false) {
        this.tweets.sort((tweetA, tweetB) => {
          const nameA = tweetA.name.toLowerCase()
          const nameB = tweetB.name.toLowerCase();
          if (nameA < nameB) return this.sort_by_name.type === 'asc' ? -1: 1;
          if (nameA > nameB) return this.sort_by_name.type === 'asc' ? 1: -1;
          return 0;
        });
      }
      if (this.sort_by_date.active === false) {
        this.tweets.sort((tweetA, tweetB) => {
          const dateA = new Date(tweetA.created_at);
          const dateB = new Date(tweetB.created_at);
          return dateA - dateB;
        });
      }
    },
    formatDate: function (string_date) {
      const date = new Date(string_date);
      return `${date.toLocaleDateString()}  ${date.toLocaleTimeString()}`;
    }
  },
  watch: {
     sort_by_name: function(val) {
       // current value will be used to decide asc or desc order
      this.tweets.sort((tweetA, tweetB) => {
        const nameA = tweetA.name.toLowerCase()
        const nameB = tweetB.name.toLowerCase();
        if (nameA < nameB) return val ? -1: 1;
        if (nameA > nameB) return val ? 1: -1;
        return 0;
      });
    },
    sort_by_date: function(val) {
      this.tweets.sort((tweetA, tweetB) => {
        const dateA = new Date(tweetA.created_at);
        const dateB = new Date(tweetB.created_at);
        return val ? dateA - dateB: dateB - dateA;
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.center {
  text-align: center;
}
.margin {
  margin-left:auto; 
  margin-right:auto;
}
.margin-bottom {
  margin-bottom: 10px;
}
</style>
