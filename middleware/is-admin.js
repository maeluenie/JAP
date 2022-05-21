export default async function({ $auth, redirect }) {
  let user = $auth.user;
  if (!$auth.loggedIn) {
    redirect("/");
  } else {
    if (user != "admin") {
      redirect("/userQA");
    }
  }
}
  