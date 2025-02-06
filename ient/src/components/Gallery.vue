<section id='about-kristoffer' class="info">
                <section id="carosel-container" class="carosel">
                </section>
                <section id='bio'class="bio-container"></section>        
                </div>
                <nav class='ext-bar'>
                    {% for key, value in links.items() %}

                        <a href='{{ value }}'>
                            <span>                           
                                <i class="bi bi-{{ key }}"></i>
                            </span>
                        </a>
                    {% endfor %}
                </nav>
                
            </section>