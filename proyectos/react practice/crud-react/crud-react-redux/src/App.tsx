import { Toaster } from "sonner";
import "./App.css";
import { CreateNewUSer } from "./components/CreateNewUser";
import ListOfUsers from "./components/ListOfUsers";

function App() {
	return (
		<>
			<ListOfUsers />
			<CreateNewUSer />
			<Toaster richColors />
		</>
	);
}

export default App;
