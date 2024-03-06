import logo from './logo.svg';
import './App.css';

export default function App() {


  function handleSubmit(event){
    event.preventDefault();
	 
    const formData = new FormData(event.target);
    const query = formData.get("query");
    console.log(query)
    // fetch ('https://nginx/api')
    // .then(response => response.json())
    // .then(data => console.log(data))
    // .then(error => console.error('Error',error))
  }

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input name="query" />
        <button type="submit"> Search</button>
        </form>
    </div>
  );
}

