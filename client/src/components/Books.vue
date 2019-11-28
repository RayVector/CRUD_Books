<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>
          Books
        </h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">
          Add Book
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Is read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title}}</td>
              <td>{{ book.author}}</td>
              <td>
                <span v-if="book.isRead">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: "Books",
    data() {
      return {
        books: []
      }
    },
    methods: {
      getBooks() {
        const path = 'http://127.0.0.1:5000/books';
        axios.get(path)
          .then((res) => {
            this.books = res.data.books;
          })
          .catch((error) => {
            console.error(error);
          })
      }
    },
    created() {
      this.getBooks();
    }
  }
</script>

<style scoped lang="css">

</style>
