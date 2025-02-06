       <footer id='footer-container'class="mb-5">
            <section class="justify-content-space-evently-row">
                <section id="footer-apps" class="justify-content-space-evently-row"></section>
                <section id="powered-by">
                </section>
            </section>
            <script>    
                //  HTML Validator FROM W3C validation services
                //  Adapted from https://stackoverflow.com/a/10162353
                document.addEventListener('DOMContentLoaded', function() {
                    const html = '<!DOCTYPE ' + document.doctype.name +
                        (document.doctype.publicId ? ' PUBLIC "' + document.doctype.publicId + '"' : '') +
                        (!document.doctype.publicId && document.doctype.systemId ? ' SYSTEM' : '') +
                        (document.doctype.systemId ? ' "' + document.doctype.systemId + '"' : '') +
                        '>\n' + document.documentElement.outerHTML;
    
                    //  Checks for HTML validations
                    document.querySelector('form[action="https://validator.w3.org/check"] > input[name="fragment"]').value = html;
                    });

                    
            </script>
        </footer>