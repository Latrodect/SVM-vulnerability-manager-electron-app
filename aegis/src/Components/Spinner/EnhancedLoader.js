import React, { Suspense } from "react";

export default function Loader(Component) {
  function Loading(params) {
    return (
      <Suspense fallback={
      <div class="ring">Wasp
      <span class="ringSpawn"></span>
    </div>
  }>
        <Component {...params} />
      </Suspense>
    );
  }
  return Loading;
}

