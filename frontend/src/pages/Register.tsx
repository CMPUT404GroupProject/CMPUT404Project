import React, { useState } from "react";
import * as Yup from "yup";
import { useFormik } from "formik";
import { useDispatch } from "react-redux";
import authSlice from "../store/slices/auth";
import axios from "axios";
import { useHistory } from "react-router";

function Register() {
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const dispatch = useDispatch();
  const history = useHistory();

  const handleLogin = (github: string, password: string, username: string) => {
    axios
      .post(`${process.env.REACT_APP_API_URL}/api/auth/register/`, { github, password, username})
      .then((res) => {
        console.log(res)
        setMessage("Account created successfully");
      })
      .catch((err) => {
        setMessage("Error creating account");
      });
  };

  const formik = useFormik({
    initialValues: {
      github: "",
      password: "",
      username: "",
    },
    onSubmit: (values) => {
      setLoading(true);
      handleLogin(values.github, values.password, values.username);
    },
    validationSchema: Yup.object({
      github: Yup.string().trim().required("?"),
      password: Yup.string().trim().required("?"),
      username: Yup.string().trim().required("?"),
    }),
  });

  return (
    <div className="h-screen flex bg-gray-bg1">
      <div className="w-full max-w-md m-auto bg-white rounded-lg border border-primaryBorder shadow-default py-10 px-16">
        <h1 className="text-2xl font-medium text-primary mt-4 mb-12 text-center">
          Register a new account
        </h1>
        <form onSubmit={formik.handleSubmit}>
          <div className="space-y-4">
            <input
              className="border-b border-gray-300 w-full px-2 h-8 rounded focus:border-blue-500"
              id="github"
              type="text"
              placeholder="GitHub Link"
              name="github"
              value={formik.values.github}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
            />
            {formik.errors.github ? <div>{formik.errors.github} </div> : null}
            <input
              className="border-b border-gray-300 w-full px-2 h-8 rounded focus:border-blue-500"
              id="password"
              type="password"
              placeholder="Create Password"
              name="password"
              value={formik.values.password}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
            />
            <input
              className="border-b border-gray-300 w-full px-2 h-8 rounded focus:border-blue-500"
              id="username"
              type="text"
              placeholder="Create username"
              name="username"
              value={formik.values.username}
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
              className="rounded border-gray-300 p-2 w-32 bg-blue-700 text-white"
            >
              Register
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Register;
