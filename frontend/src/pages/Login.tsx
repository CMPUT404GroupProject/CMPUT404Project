import React, { useState } from "react";
import * as Yup from "yup";
import { useFormik } from "formik";
import { useDispatch } from "react-redux";
import authSlice from "../store/slices/auth";
import axios from "axios";
import { useHistory } from "react-router";

function Login() {
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const dispatch = useDispatch();
  const history = useHistory();

  const handleLogin = (displayName: string, password: string) => {
    console.log(displayName);
    axios
      .post(`${process.env.REACT_APP_API_URL}/api/auth/login/`, { displayName, password })
      .then((res) => {
        dispatch(
          authSlice.actions.setAuthTokens({
            token: res.data.access,
            refreshToken: res.data.refresh,
          })
        );
        dispatch(authSlice.actions.setAccount(res.data.user));
        setLoading(false);
        history.push("/", {
          userId: res.data.id
        });
      })
      .catch((err) => {
        setMessage(err.response.data.detail.toString());
      });
  };

  const formik = useFormik({
    initialValues: {
      displayName: "",
      password: "",
    },
    onSubmit: (values) => {
      setLoading(true);
      handleLogin(values.displayName, values.password);
    },
    validationSchema: Yup.object({
      displayName: Yup.string().trim().required("?"),
      password: Yup.string().trim().required("?"),
    }),
  });

  return (
    <div className="h-screen flex bg-gray-bg1">
      <div className="w-full max-w-md m-auto bg-white rounded-lg border border-primaryBorder shadow-default py-10 px-16">
        <h1 className="text-2xl font-medium text-primary mt-4 mb-12 text-center">
          Log in to your account
        </h1>
        <form onSubmit={formik.handleSubmit}>
          <div className="space-y-4">
            <input
              className="border-b border-gray-300 w-full px-2 h-8 rounded focus:border-blue-500"
              id="displayName"
              type="text"
              placeholder="Display Name"
              name="displayName"
              value={formik.values.displayName}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
            />
            {formik.errors.displayName ? <div>{formik.errors.displayName} </div> : null}
            <input
              className="border-b border-gray-300 w-full px-2 h-8 rounded focus:border-blue-500"
              id="password"
              type="password"
              placeholder="Password"
              name="password"
              value={formik.values.password}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
            />
            {formik.errors.password ? (
              <div>{formik.errors.password} </div>
            ) : null}
          </div>
          <div className="text-danger text-center my-2" hidden={false}>
            {message}
          </div>

          <div className="flex justify-center items-center mt-6">
            <button
              type="submit"
              disabled={loading}
              className="rounded border-gray-300 p-2 w-32 bg-blue-700 text-white LoginButton"
            >
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Login;
