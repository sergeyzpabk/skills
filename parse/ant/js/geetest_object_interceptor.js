(function(){var e={};if(typeof items!=="undefined"){e=items}else{if(document.currentScript&&document.currentScript.dataset&&document.currentScript.dataset["parameters"]){try{e=JSON.parse(document.currentScript.dataset["parameters"])}catch(e){}}}var r=typeof e!=="undefined"&&e.delay_onready_callback;var a={};var i;var t;var c=false;Object.defineProperty(window,"initGeetest",{get:function(){return n},set:function(e){t=e},configurable:true});var n=function(n,e){var o=function(){window.postMessagePosteRestante("geetestContentScript",{type:"solveGeetestCaptcha",geetestParameters:{gt:n.gt,challenge:n.challenge,api_server:n.api_server,appendToSelector:n.appendToSelector,getLib:n.getLib}},window.location.href);c=true};var t={appendTo:function(e){if(n.product!=="bind"){var t=d(e);n.appendToSelector=t;s(t);o();setTimeout(function(){if(!r&&typeof a.onReady==="function"){a.onReady()}},100)}return this},bindForm:function(e){var t=d(e);n.appendToSelector=t;s(t);if(i){u(n.appendToSelector,i)}},onReady:function(e){a.onReady=e;if(n.product==="bind"){if(typeof a.onReady==="function"){a.onReady()}}return this},onSuccess:function(e){a.onSuccessCallback=e;return this},onError:function(e){a.onError=e;return this},onClose:function(e){a.onClose=e;return this},getValidate:function(){s(n.appendToSelector);u(n.appendToSelector,i);return{geetest_challenge:i.challenge,geetest_validate:i.validate,geetest_seccode:i.seccode}},reset:function(){if(c){}},destroy:function(){f(n.appendToSelector)},verify:function(){o()}};if(typeof e==="function"){e(t)}window.addEventListener("message",function(e){if(!e.data||typeof e.data.receiver=="undefined"||e.data.receiver!="geetestObjectInterceptor"){return}var t=e.data;if(t.type==="geetestTaskSolution"){i=e.data.taskSolution;if(!r){u(n.appendToSelector,i);if(typeof a.onSuccessCallback==="function"){a.onSuccessCallback()}}else{if(typeof a.onReady==="function"){a.onReady()}setTimeout(()=>{u(n.appendToSelector,i);if(typeof a.onSuccessCallback==="function"){a.onSuccessCallback()}},Math.round(2e3+Math.random()*2e3))}}else if(t.type==="geetestError"){if(typeof a.onError==="function"){a.onError(typeof t.error!=="undefined"?t.error:{})}}})};function d(e){var t;if(typeof e==="object"&&typeof e.appendChild!=="undefined"){if(e.id){t="#"+e.id}else{var n=document.createElement(e.tagName);n.id="antcpt"+Math.round(Math.random()*1e3);e.appendChild(n);t="#"+n.id}}else if(typeof e==="string"){t=e}else{}return t}function s(e){if(e&&typeof document.querySelector==="function"){var t=l(e);if(t&&t.getElementsByClassName("geetest_form")&&t.getElementsByClassName("geetest_form").length==0){t.insertAdjacentHTML("beforeend",'<div class="geetest_holder geetest_wind geetest_detect" style="width: 300px;">\n'+'    <div class="geetest_form">\n'+'        <input type="hidden" name="geetest_challenge">\n'+'        <input type="hidden" name="geetest_validate">\n'+'        <input type="hidden" name="geetest_seccode">\n'+"    </div>\n"+"</div>")}}}function f(e){if(e&&typeof document.querySelector==="function"){var t=l(e);if(t){var n=t.getElementsByClassName("geetest_holder");if(n&&n.length){Array.from(n).forEach(e=>e.parentElement.removeChild(e))}}}}function u(e,t){if(e&&typeof document.querySelector==="function"){var n=l(e+" input[name=geetest_challenge]");var o=l(e+" input[name=geetest_validate]");var r=l(e+" input[name=geetest_seccode]");if(n){n.value=t.challenge}if(o){o.value=t.validate}if(r){r.value=t.seccode}}}function l(t){try{return document.querySelector(t)}catch(e){if(typeof CSS.escape==="function"){return document.querySelector(CSS.escape(t))}}}})();