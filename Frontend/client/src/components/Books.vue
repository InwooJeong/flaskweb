<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <alert2 :message="message" v-if="showMessage2"></alert2>
        <button 
          type="button" 
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal">
          Add Book
        </button>
        <br><br>

        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          
          <tbody v-if="books.length>0">
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button 
                    type="button" 
                    class="btn btn-warning btn-sm"
                    @click="toggleUpdateBookModal(book)">
                    Update
                  </button>
                  <button 
                    type="button" 
                    class="btn btn-danger btn-sm"
                    @click="handleDeleteBook(book)">
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>

          <tbody v-if="books.length<1">
            <tr>
              <td colspan="3">You don't have any book! please add one</td>
            </tr>
          </tbody>

        </table>
      </div>
    </div>
  </div>

  <!-- Modal(add book) Start -->
  <div
    ref="addBookModal"
    class="modal fade"
    :class="{show: activeAddBookModal,'d-block': activeAddBookModal}"
    tableindex="-1"
    role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        
        <div class="modal-header">
          <h5 class="modal-title">Add a new book</h5>
          <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
            @click="toggleAddBookModal">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>

        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="addBookTitle" class="form-label">Title:</label>
              <input
                type="text"
                class="form-control"
                id="addBookTitle"
                v-model="addBookForm.title"
                placeholder="Enter title">
            </div>
            <div class="mb-3">
              <label for="addBookAuthor" class="form-label">Author:</label>
              <input
                type="text"
                class="form-control"
                id="addBookAuthor"
                v-model="addBookForm.author"
                placeholder="Enter author">
            </div>
            <div class="mb-3 form-check">
              <input
                type="checkbox"
                class="form-check-input"
                id="addBookRead"
                v-model="addBookForm.read">
                <label class="form-check-label" for="addBookRead">Read?</label>
            </div>
            <div class="btn-group" role="group">
              <button
                type="button"
                class="btn btn-primary btn-sm"
                @click="handleAddSubmit">
                submit
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="handleAddReset">
                reset
              </button>
            </div>
          </form>
        </div>

      </div>
    </div>

  </div>
  <!-- Modal(add book) End -->

  <!-- Modal(update book) Start -->
  <div
    ref="updateBookModal"
    class="modal fade"
    :class="{show: activeUpdateBookModal,'d-block': activeUpdateBookModal}"
    tableindex="-1"
    role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        
        <div class="modal-header">
          <h5 class="modal-title">Update</h5>
          <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
            @click="toggleUpdateBookModal">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>

        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="updateBookTitle" class="form-label">Title:</label>
              <input
                type="text"
                class="form-control"
                id="updateBookTitle"
                v-model="updateBookForm.title"
                placeholder="Enter title">
            </div>
            <div class="mb-3">
              <label for="updateBookAuthor" class="form-label">Author:</label>
              <input
                type="text"
                class="form-control"
                id="updateBookAuthor"
                v-model="updateBookForm.author"
                placeholder="Enter author">
            </div>
            <div class="mb-3 form-check">
              <input
                type="checkbox"
                class="form-check-input"
                id="updateBookRead"
                v-model="updateBookForm.read">
                <label class="form-check-label" for="updateBookRead">Read?</label>
            </div>
            <div class="btn-group" role="group">
              <button
                type="button"
                class="btn btn-primary btn-sm"
                @click="handleUpdateSubmit">
                submit
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="handleUpdateCancel">
                reset
              </button>
            </div>
          </form>
        </div>

      </div>
    </div>

  </div>
  <div v-if="activeUpdateBookModal" class="modal-backdrop fade show"></div>
  <!-- Modal(update book) End -->
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import AlertDanger from './AlertDanger.vue';

export default{
  data(){
    return{
      activeAddBookModal: false,
      activeUpdateBookModal: false,
      updateBookForm: {
        id:'',
        title:'',
        author:'',
        read:[],
      },
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
      books: [],
      message: '',
      showMessage: false,
      showMessage2: false,
    };
  },
  components: {
    alert: Alert,
    alert2: AlertDanger,
  },
  methods:{
    addBook(payload){
      const path = `http://localhost:5000/books`;
      axios.post(path, payload)
        .then(()=>{
          this.getBooks();
          this.message = 'Book added!';
          this.showMessage = true;
          setTimeout(()=>{
            this.showMessage = false;
          },3000);
        })
        .catch((error)=>{
          console.error(error)
          this.getBooks();
          this.message = 'Book add failed!';
          this.showMessage2 = true;
          setTimeout(()=>{
            this.showMessage2 = false;
          },3000);
        });
    },
    getBooks(){
      const path = `http://localhost:5000/books`;
      axios.get(path)
        .then((res)=>{
          this.books = res.data.books;
        })
        .catch((error)=>{
          console.error(error);
        });
    },
    updateBook(payload,bookID){
      const path = `http://localhost:5000/books/${bookID}`;
      axios.put(path,payload)
        .then(()=>{
          this.getBooks();
          console.log("update axios");
          this.message = 'Book updated!';
          this.showMessage = true;
          setTimeout(()=>{
            this.showMessage = false;
          },3000);
        })
        .catch((error)=>{
          console.error(error);
          this.getBooks();
        });
    },
    removeBook(bookID){
      const path = `http://localhost:5000/books/${bookID}`;
      axios.delete(path)
        .then(()=>{
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
          setTimeout(()=>{
            this.showMessage = false;
          },3000);
        })
        .catch((error)=>{
            console.error(error);
            this.getBooks();
        });
    },
    handleAddReset(){
      this.initForm();
    },
    handleUpdateCancel(){
      this.toggleUpdateBookModal(null);
      this.initForm();
      this.getBooks();
    },
    handleAddSubmit(){
      this.toggleAddBookModal();
      let read = false;
      if (this.addBookForm.read[0]){
        read = true;
      }
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    initForm(){
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
      this.updateBookForm.id = '';
      this.updateBookForm.title = '';
      this.updateBookForm.author = '';
      this.updateBookForm.read = [];
    },
    toggleAddBookModal(){
      const body = document.querySelector('body');
      this.activeAddBookModal = !this.activeAddBookModal;
      if(this.activeAddBookModal){
        body.classList.add('modal-open');
      }else{
        body.classList.remove('modal-open');
      }
    },
    toggleUpdateBookModal(book){
      if(book){
        this.updateBookForm = book;
      }
      const body = document.querySelector('body');
      this.activeUpdateBookModal = !this.activeUpdateBookModal;
      if(this.activeUpdateBookModal){
        body.classList.add('modal-open');
      }else{
        body.classList.remove('modal-open');
      }
    },
    handleUpdateSubmit(){
      this.toggleUpdateBookModal(null);
      let read = false;
      if(this.updateBookForm.read) read = true;
      const payload = {
        title: this.updateBookForm.title,
        author: this.updateBookForm.author,
        read,
      };
      this.updateBook(payload, this.updateBookForm.id);
    },
    handleDeleteBook(book){
      if(confirm('Do you really wanna delete this book?')){
        this.removeBook(book.id)
      }
    },
  },
  created(){
    this.getBooks();
  },
};
</script>