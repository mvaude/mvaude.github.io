use std::rc::Rc;
use yew::prelude::*;
use yewtil::NeqAssign;

use crate::education::EducationComponent;
use crate::experience::ExperienceComponent;
use crate::location::LocationComponent;
use crate::phone_number::PhoneNumberComponent;
use crate::protos::resume::AboutMe;
use crate::protos::resume::Resume;
use crate::skills::SkillComponent;

#[derive(Clone, Properties, PartialEq)]
pub struct ResumeProps {
    pub resume: Rc<Resume>,
}

pub enum Msg {
    Hover(AboutMe),
    Clear,
}

pub struct ResumeComponent {
    props: ResumeProps,
    link: ComponentLink<Self>,
    am_hover: bool,
    am_hovered: Option<AboutMe>,
}

impl Component for ResumeComponent {
    type Message = Msg;
    type Properties = ResumeProps;

    fn create(props: Self::Properties, link: ComponentLink<Self>) -> Self {
        ResumeComponent {
            props,
            link,
            am_hover: false,
            am_hovered: None,
        }
    }

    fn update(&mut self, msg: Self::Message) -> ShouldRender {
        match msg {
            Msg::Hover(am) => self.am_hovered = Some(am),
            Msg::Clear => self.am_hovered = None,
        };
        true
    }

    fn change(&mut self, props: Self::Properties) -> ShouldRender {
        self.props.neq_assign(props)
    }

    fn view(&self) -> Html {
        let res = &self.props.resume;
        let github = format!("github.com/{}", res.get_github_profile());
        let linkedin = format!("linkedin.com/in/{}/", res.get_linkedin_profile());
        let split: Vec<&str> = linkedin.rsplitn(2, '-').collect();
        let linkedin_short = split[1];
        let phone = res.get_phone_number().clone();
        let location = res.get_location().clone();
        let aboutme = res.get_about_me().to_vec();
        let education = res.get_education().to_vec();
        let experience = res.get_experience().to_vec();
        let skills = res.get_skills().to_vec();

        let am_class = if self.am_hover {
            "am-hover am-list"
        } else {
            "am-list"
        };

        html! {
            <div class="content">
                <header class="main-header">
                    <h1 class="main-header-name">{ res.get_name().to_ascii_uppercase() }</h1>
                    <ul class="main-header-list">
                        <li><i class="fas fa-envelope"></i>{ res.get_email() }</li>
                        <li><PhoneNumberComponent phone=phone /></li>
                        <li><a href=format!("https://{}", &github)>
                            <i class="fab fa-github"></i>{ github }</a></li>
                        <li><a href=format!("https://{}", &linkedin)>
                            <i class="fab fa-linkedin-in"></i>{ linkedin_short }</a></li>
                        <li><LocationComponent location=location /></li>
                    </ul>
                </header>
                <div class="main-column main-left">
                    <SkillComponent skills=skills/>
                    <EducationComponent education=education />
                    { self.view_links() }
                </div>
                <div class="main-column main-right">
                    <h2>{ "ABOUT ME"}</h2>
                    <div class="about-me">
                        <ul class=am_class>
                            { for aboutme.iter().map(|am| self.view_about_me(am)) }
                        </ul>
                    </div>
                    <ExperienceComponent experience=experience/>
                </div>
            </div>
        }
    }
}

impl ResumeComponent {
    fn view_links(&self) -> Html {
        let res = &self.props.resume;
        let source_code = res.get_source_code();
        let source_code_https = format!("https://{}", source_code);
        let host_link = res.get_host_link();
        let host_link_https = format!("https://{}", host_link.clone());
        let pdf_name = format!("https://raw.githubusercontent.com/{}/master/{}-Resume.pdf", source_code.split_once("/").unwrap().1, res.name.replace(" ", ""));
        html! {
            <div class="links">
                <h2>{ "LINKS" }</h2>
                <ul class="links-list">
                    <li class="screen-only">
                        <a href=pdf_name target="_blank">
                            <i class="fa fa-external-link" aria-hidden="true"></i>
                            { "Download a PDF of this resume" }
                        </a>
                    </li>
                    <li class="screen-only">
                        <a href=source_code_https.clone()>
                            <i class="fa fa-external-link" aria-hidden="true"></i>
                            { "View the source code" }
                        </a>
                    </li>
                    <li class="print-only">
                        { "View this resume as a WebAssembly app:" }
                        <br/>
                        <a href=host_link_https>
                            <i class="fa fa-external-link" aria-hidden="true"></i>
                            { host_link }
                        </a>
                    </li>
                    <li class="print-only">
                        { "View the source code:" }
                        <br/>
                        <a href=source_code_https>
                            <i class="fa fa-external-link" aria-hidden="true"></i>
                            { source_code }
                        </a>
                    </li>
                </ul>
            </div>
        }
    }

    fn view_about_me(&self, am: &AboutMe) -> Html {
        let send_am = am.clone();
        let publish_am = am.clone();
        let mouseover = self.link.callback(move |_| Msg::Hover(send_am.to_owned()));
        let mouseout = self.link.callback(|_| Msg::Clear);
        let mut class = "am-item";
        if let Some(hov_am) = &self.am_hovered {
            if hov_am == am {
                class = "am-item am-hover"
            }
        }
        html! {
            <li class=class onmouseover=mouseover onmouseout=mouseout>
                { publish_am.description }
            </li>
        }
    }
}
