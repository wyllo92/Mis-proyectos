import { createSlice, type PayloadAction } from "@reduxjs/toolkit";

const DEFAULT_STATE = [
	{
		id: "1",
		name: "pepito perez",
		email: "perez@gmail.com",
		github: "perez1012",
	},
	{
		id: "2",
		name: "pablo landa",
		email: "landa@gmail.com",
		github: "landa373",
	},
	{
		id: "3",
		name: "geronimo castro",
		email: "castro@gmail.com",
		github: "castra636",
	},
	{
		id: "4",
		name: "juana la babana",
		email: "labanana@gmail.com",
		github: " ",
	},
	{
		id: "5",
		name: "homer sanchez",
		email: "sanchez@gmail.com",
		github: "homersan34",
	},
	{
		id: "6",
		name: "maria luz",
		email: "mariluz@gmail.com",
		github: "midudev",
	},
];

export type UserId = string;

export interface user {
	name: string;
	email: string;
	github: string;
}

export interface UserWithId extends user {
	id: UserId;
}

const initialState: UserWithId[] = (() => {
	const persistedState = localStorage.getItem("__redux__state__");
	if (persistedState) {
		return JSON.parse(persistedState).users;
	}
	return DEFAULT_STATE;
})();

export const usersSlice = createSlice({
	name: "users",
	initialState,
	reducers: {
		addNewUser: (state, action: PayloadAction<user>) => {
			const id = crypto.randomUUID();
			return [...state, { id, ...action.payload }];
		},

		deleteUserById: (state, action: PayloadAction<UserId>) => {
			const id = action.payload;
			return state.filter((user) => user.id !== id);
		},
	},
});

export default usersSlice.reducer;

export const { addNewUser, deleteUserById } = usersSlice.actions;
