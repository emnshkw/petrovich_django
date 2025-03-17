'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"flutter_bootstrap.js": "2430682a8b8526c0db3fa8a0d9122579",
"version.json": "5d7ecae0594ba2c077cfd2d7e101f520",
"index.html": "d27a333269fb784426a31e9d95b827c0",
"/": "d27a333269fb784426a31e9d95b827c0",
"main.dart.js": "1cff048335ca4267aecfcc27e6ec538a",
"flutter.js": "f393d3c16b631f36852323de8e583132",
"icons/favicon-16x16.png": "1a32ee86382989bb65c595eefb2c7f07",
"icons/favicon.ico": "49d53bc31c69dff7b54f0de7ed736d4b",
"icons/apple-touch-icon.png": "9edc5c9770f5631fc6eca6c08d15c45a",
"icons/Icon-192.png": "1d103c33d13c966a4cbc27b95a5f0541",
"icons/favicon.png": "5dcef449791fa27946b3d35ad8803796",
"icons/Icon-512.png": "92b7c9aa170f7ed00f1d24ac44297b74",
"icons/favicon-32x32.png": "e0d28f9f8ecade6a1d4c51afb2bf3050",
"manifest.json": "222cbc381ec18f79cdec99dbcb7b78d6",
"assets/AssetManifest.json": "2a64dccf5d9b0bdb88fac78f006f0d6a",
"assets/NOTICES": "0e811d6d956edfb12ff2534726d8654c",
"assets/FontManifest.json": "6d2ebdf95d05b8c99f88630c4f458c46",
"assets/AssetManifest.bin.json": "8afd334672077ff051a1e25aa64a24a7",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "e986ebe42ef785b27164c36a9abc7818",
"assets/packages/fluttertoast/assets/toastify.js": "56e2c9cedd97f10e7e5f1cebd85d53e3",
"assets/packages/fluttertoast/assets/toastify.css": "a85675050054f179444bc5ad70ffc635",
"assets/shaders/ink_sparkle.frag": "ecc85a2e95f5e9f53123dcaf8cb9b6ce",
"assets/AssetManifest.bin": "d9c4ac905e59d4e3fb5ace7c41ccadea",
"assets/fonts/MaterialIcons-Regular.otf": "662a5bc22523e2fce86f2b184039abe8",
"assets/assets/photos/Rainbow1.jpeg": "baf87dc724a14df11fea3f62a1c69f65",
"assets/assets/photos/Ysadba1.jpeg": "8eafeaa71665c83e469b8e893974a982",
"assets/assets/photos/Banket1.jpeg": "b63598fd1094270e29cf567238a21b2d",
"assets/assets/photos/House_on_tree1.jpeg": "e370ba1aab302d830f826eb8418e5f37",
"assets/assets/photos/reserv.png": "fa248faff18f6a8d91c72cf903bc06ef",
"assets/assets/photos/logo.png": "8d20b08085b67de2a160973991ca6af1",
"assets/assets/photos/Mechta1.jpeg": "5339845edc67e905b97fe46510a4b164",
"assets/assets/photos/Izbushka1.jpeg": "97e8c7e97ba04f12dc1fd7466e784185",
"assets/assets/photos/Plavuchii1.jpeg": "32fc91432f625cc9a64eb76961ea2417",
"assets/assets/photos/Vigvam2.jpg": "9315d1f86833b7555fe6e6503b4379f4",
"assets/assets/photos/Vigvam3.jpg": "d1104af98717cd6fa19ed09f400f2ab4",
"assets/assets/photos/Vigvam1.jpg": "d4bb587dc3e5f2418afe1b5488231113",
"assets/assets/photos/image1.png": "78d22de0fe93510ea0361eb91e4a6c03",
"assets/assets/photos/Vigvam4.jpg": "69451b5b67e44c9e551034189977fa39",
"assets/assets/photos/Vigvam5.jpg": "147df0782b3510c90685a283667e2dc8",
"assets/assets/photos/smile.png": "7a9b8beaff904927e98b44c83d38e183",
"assets/assets/photos/image.png": "54b481fa6e74bd4aeb6cec154ec4157c",
"assets/assets/fonts/TildaSans-Semibold.ttf": "b8aa7037bb769ed7740211ef7d5fccc9",
"assets/assets/fonts/TildaSans-Regular.ttf": "279e2ab4ce6408d48b57e998c7674c1f",
"assets/assets/fonts/TildaSans-Light.ttf": "75e1916f22b00fd33f612bda8b307886",
"assets/assets/fonts/SocialIcons.ttf": "f393c49e3459f645152cd7e823683bd6",
"assets/assets/fonts/TildaSans-Bold.ttf": "3b3b7d02957ce765508f8d700fa7e3e8",
"assets/assets/fonts/TildaSans-Black.ttf": "6755b8d1df07add816ea630ddf10024d",
"assets/assets/fonts/TildaSans-Medium.ttf": "065a2d909529525609dccb537c51e13f",
"assets/assets/fonts/TildaSans-ExtraBold.ttf": "32c82df7ddb9f83fd5770486b7706763",
"canvaskit/skwasm.js": "694fda5704053957c2594de355805228",
"canvaskit/skwasm.js.symbols": "262f4827a1317abb59d71d6c587a93e2",
"canvaskit/canvaskit.js.symbols": "48c83a2ce573d9692e8d970e288d75f7",
"canvaskit/skwasm.wasm": "9f0c0c02b82a910d12ce0543ec130e60",
"canvaskit/chromium/canvaskit.js.symbols": "a012ed99ccba193cf96bb2643003f6fc",
"canvaskit/chromium/canvaskit.js": "671c6b4f8fcc199dcc551c7bb125f239",
"canvaskit/chromium/canvaskit.wasm": "b1ac05b29c127d86df4bcfbf50dd902a",
"canvaskit/canvaskit.js": "66177750aff65a66cb07bb44b8c6422b",
"canvaskit/canvaskit.wasm": "1f237a213d7370cf95f443d896176460",
"canvaskit/skwasm.worker.js": "89990e8c92bcb123999aa81f7e203b1c"};
// The application shell files that are downloaded before a service worker can
// start.
const CORE = ["main.dart.js",
"index.html",
"flutter_bootstrap.js",
"assets/AssetManifest.bin.json",
"assets/FontManifest.json"];

// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});
// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        // Claim client to enable caching on first launch
        self.clients.claim();
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      // Claim client to enable caching on first launch
      self.clients.claim();
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});
// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});
self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});
// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}
// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
